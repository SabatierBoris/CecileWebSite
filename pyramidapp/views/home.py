"""
The page
"""
from pyramid.view import view_config


@view_config(route_name='home', renderer='home.mak')
def home(request):
    """
    Bouboup
    """

    request = request
    return {}
