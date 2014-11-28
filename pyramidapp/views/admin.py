"""
The home admin view part
"""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.threadlocal import get_current_registry
from pyramid.interfaces import IRouteRequest, IViewClassifier, ISecuredView
from zope.interface.declarations import providedBy


class AdminView(object):
    """
    The home admin view logic
    """
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home_admin',
                 renderer='admin/home.mak')
    def home(self):
        """
        List the administration page depending of the user right
        """
        all_admin_pages = {'Rights': 'right_list',
                           'Groups': 'group_list',
                           'Users': 'user_list'}

        accessible_pages = {}

        for page in all_admin_pages:
            if self.is_allowed_to_view(all_admin_pages[page]).boolval:
                accessible_pages[page] = all_admin_pages[page]

        if accessible_pages == []:
            return HTTPFound(self.request.route_url('login'))

        return {'title': 'Administration', 'pages': accessible_pages}

    def is_allowed_to_view(self, view_name):
        """
        Check if the current user have the right to the view
        """
        try:
            reg = self.request.registry
        except AttributeError:
            reg = get_current_registry()

        request_iface = reg.queryUtility(IRouteRequest, name=view_name)
        provides = [IViewClassifier,
                    request_iface,
                    providedBy(self.request.context)]
        view = reg.adapters.lookup(provides, ISecuredView, name='')

        assert view is not None
        return view.__permitted__(self.request.context, self.request)
