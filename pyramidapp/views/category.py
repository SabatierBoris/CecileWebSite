# coding : utf-8
"""
The right view part
"""
from pyramid.view import view_config

from pyramidapp.models.menu import MenuAdministration


class CategoryView(object):
    """
    The category view logic
    """
    def __init__(self, request):
        self.request = request

    @view_config(route_name='view_category',
                 renderer='home.mak')
    def view_category(self):
        """
        Display the content of a category
        """
        uid = int(self.request.matchdict.get('uid', -1))
        name = self.request.matchdict.get('name', '')

        return {}

    @MenuAdministration(order=1,
                        display='Nouvelle categorie',
                        route_name='new_category',
                        route_name_category='new_sub_category')
    @view_config(route_name='new_category',
                 # renderer='admin/category.mak',
                 renderer='home.mak',
                 permission='write')
    def new_category(self):
        """
        Display the content of a category
        """
        return {}
