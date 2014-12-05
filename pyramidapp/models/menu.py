# vim: set fileencoding=utf-8 :
"""
menu module
"""
from pyramid.threadlocal import get_current_registry
from pyramid.interfaces import IRouteRequest, IViewClassifier, ISecuredView
from zope.interface.declarations import providedBy
from pyramid.events import subscriber, BeforeRender
import logging
from pyramidapp.models.category import Category
LOG = logging.getLogger(__name__)


class MenuItem(object):
    # pylint: disable=R0903
    """
    Item of the administration menu
    """
    def __init__(self, display, route_name_category, route_name):
        self.display = display
        self.route_name_category = route_name_category
        self.route_name = route_name
        self.url = None


class MenuAdministration(object):
    # pylint: disable=R0903
    """
    Menu Administration decorator to generat automaticaly menu
    """
    PAGES = {}

    def __init__(self, order, display, route_name_category, route_name):
        """
        Constructor
        """
        val = MenuItem(display, route_name_category, route_name)
        if order in MenuAdministration.PAGES:
            LOG.warning("Order %s is already exist (%s - %s) and (%s - %s)",
                        order, route_name_category, route_name,
                        MenuAdministration.PAGES[order].route_name_category,
                        MenuAdministration.PAGES[order].route_name)
        MenuAdministration.PAGES[order] = val

    def __call__(self, func):
        """
        Decorator
        """
        return func

    @staticmethod
    def is_allowed_to_view(request, view_name):
        """
        Check if the current user have the right to the view
        """
        try:
            reg = request.registry
        except AttributeError:
            reg = get_current_registry()

        request_iface = reg.queryUtility(IRouteRequest, name=view_name)
        provides = [IViewClassifier,
                    request_iface,
                    providedBy(request.context)]
        view = reg.adapters.lookup(provides, ISecuredView, name='')

        assert view is not None
        return view.__permitted__(request.context, request)

    @classmethod
    def get_allowed_administration_page(cls, event):
        """
        Get all accecible administration page
        """
        accessible_pages = {}
        request = event['request']
        idcategory = event.rendering_val.get('idCategory', None)
        namecategory = event.rendering_val.get('nameCategory', None)

        for page in cls.PAGES:
            item = cls.PAGES[page]
            item.url = None
            if item.route_name_category and \
               idcategory and \
               namecategory and \
               cls.is_allowed_to_view(request, item.route_name_category):
                item.url = request.route_url(item.route_name_category,
                                             idCategory=idcategory,
                                             nameCategory=namecategory)
            elif item.route_name and \
                    cls.is_allowed_to_view(request, item.route_name):
                item.url = request.route_url(item.route_name)

        for key, value in cls.PAGES.items():
            if value.url:
                accessible_pages[key] = value
        return accessible_pages


class CategoryMenuItem(object):
    # pylint: disable=R0903
    """
    Category menu item
    """
    def __init__(self, category):
        self.category = category
        self.sublist = {}


def get_categories_menu(event):
    """
    Get the categories menu with sub categories
    """
    def get_menu(parent, target):
        """
        Function to get the category of a level to a target
        """
        menu = {}
        categories = Category.get_with_direct_parent(parent)

        for category in categories:
            menu[category.uid] = CategoryMenuItem(category)
            if target and target.is_a_child_of(category):
                menu[category.uid].sublist = get_menu(category, target)
        return menu

    idcategory = event.rendering_val.get('idCategory', None)
    target = Category.by_uid(idcategory)
    return get_menu(None, target)


@subscriber(BeforeRender)
def add_global(event):
    """
    Add the administration_pages for all render
    """
    pages = MenuAdministration.get_allowed_administration_page(event)
    categories = get_categories_menu(event)
    event['administration_pages'] = pages
    event['categories_pages'] = categories
