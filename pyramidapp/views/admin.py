"""
The home admin view part
"""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramidapp.models.security import is_allowed_to_view


class AdminView(object):
    # pylint: disable=R0903
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
            if is_allowed_to_view(self.request, all_admin_pages[page]).boolval:
                accessible_pages[page] = all_admin_pages[page]

        if accessible_pages == {}:
            return HTTPFound(self.request.route_url('login'))

        return {'title': 'Administration', 'pages': accessible_pages}
