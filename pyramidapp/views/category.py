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
        idcategory = int(self.request.matchdict.get('idCategory', -1))
        namecategory = self.request.matchdict.get('nameCategory', '')

        return {'idCategory': idcategory,
                'nameCategory': namecategory}

    @MenuAdministration(order=1,
                        display='Nouvelle categorie',
                        route_name='new_category',
                        route_name_category='new_sub_category')
    @view_config(route_name='new_sub_category',
                 # renderer='admin/category.mak',
                 renderer='home.mak',
                 permission='write')
    @view_config(route_name='new_category',
                 # renderer='admin/category.mak',
                 renderer='home.mak',
                 permission='write')
    def new_category(self):
        """
        Display the content of a category
        """
        idcategory = int(self.request.matchdict.get('idCategory', -1))
        namecategory = self.request.matchdict.get('nameCategory', None)

        return {'idCategory': idcategory,
                'nameCategory': namecategory}
