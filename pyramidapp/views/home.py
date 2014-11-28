"""
The page
"""
from pyramid.view import view_config
from pyramidapp.models.security import get_allowed_administration_page


@view_config(route_name='home', renderer='home.mak')
def home(request):
    """
    Bouboup
    """
    request = request
    return {}
