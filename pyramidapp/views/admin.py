"""
The home admin view part
"""
from pyramid.view import view_config


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
        self = self
        accessible_pages = {}

        return {'title': 'Administration', 'pages': accessible_pages}
