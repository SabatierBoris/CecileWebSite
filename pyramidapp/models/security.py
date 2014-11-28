# coding : utf-8
"""
Security module
"""

from pyramid.security import Allow
from pyramid.threadlocal import get_current_registry
from pyramid.interfaces import IRouteRequest, IViewClassifier, ISecuredView
from zope.interface.declarations import providedBy
from pyramid.events import subscriber, BeforeRender

from pyramidapp.models.user import User
from pyramidapp.models.group import Group


class MenuAdministration(object):
    # pylint: disable=R0903
    """
    Menu Administration decorator to generat automaticaly menu
    """
    PAGES = {}

    def __init__(self, display, route_name):
        """
        Constructor
        """
        MenuAdministration.PAGES[display] = route_name

    def __call__(self, func):
        """
        Decorator
        """
        return func


def groups_finder(login, request):
    """
    Function to know the groups of a user
    Used by security module of pyramid
    """
    # Has 3 potential returns:
    #     - None, meaning userid doesn't exist
    #     - An empty list, meaning existing user but no group
    #     - List of groups for that userid
    user = User.by_login(login)
    request = request
    if user is None:
        return
    for group in user.groups:
        yield group.name


class ACL(object):
    # pylint: disable=R0903
    """
    Class list like for ACL access managed with BDD
    """
    def __len__(self):
        """
        Get the number of ACL
        """
        size = 0
        for group in Group.all():
            size += len(group.rights)
        return size

    def __getitem__(self, key):
        """
        Get the ACL number @key
        """
        i = 0
        for val in self:
            if i == key:
                return val
            i += 1

    def __iter__(self):
        """
        Get a iterator of ACL
        """
        for group in Group.all():
            for right in group.rights:
                yield(Allow, group.name, right.name)


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


def get_allowed_administration_page(request):
    """
    Get all accecible administration page
    """
    accessible_pages = {}

    for page in MenuAdministration.PAGES:
        if is_allowed_to_view(request, MenuAdministration.PAGES[page]).boolval:
            accessible_pages[page] = MenuAdministration.PAGES[page]

    return accessible_pages


@subscriber(BeforeRender)
def add_global(event):
    """
    Add the administration_pages for all render
    """
    pages = get_allowed_administration_page(event['request'])
    event['administration_pages'] = pages
