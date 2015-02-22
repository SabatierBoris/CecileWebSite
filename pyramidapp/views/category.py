# vim: set fileencoding=utf-8 :
"""
The category view part
"""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from sqlalchemy.exc import IntegrityError

from pyramidapp.models.menu import MenuAdministration
from pyramidapp.models.category import Category
from pyramidapp.models.mypaginate import MyPage
from pyramidapp.forms.category import CategoryForm


class CategoryView(object):
    """
    The category view logic
    """
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='home.mak')
    @view_config(route_name='view_category',
                 renderer='home.mak')
    def view_category(self):
        """
        Display the content of a category
        """
        idcategory = int(self.request.matchdict.get('idCategory', -1))
        namecategory = self.request.matchdict.get('nameCategory', '')
        current_page = self.request.GET.get('page', 1)

        category = Category.by_uid(idcategory)
        contents = None
        if category:
            contents = list(category.get_content())
        else:
            contents = Category.get_with_direct_parent(None)
        paginated_contents = MyPage(contents,
                                    page=current_page,
                                    items_per_page=12)

        return {'idCategory': idcategory,
                'nameCategory': namecategory,
                'contents': paginated_contents,
                'pagesLink': paginated_contents.get_pages(url='?page=$page')}

    @MenuAdministration(order=1,
                        display='Nouvelle categorie',
                        route_name='new_category',
                        route_name_category='new_sub_category')
    @view_config(route_name='new_sub_category',
                 renderer='admin/category.mak',
                 permission='write')
    @view_config(route_name='new_category',
                 renderer='admin/category.mak',
                 permission='write')
    def new_category(self):
        """
        Display the content of a category
        """
        idcategory = int(self.request.matchdict.get('idCategory', -1))
        namecategory = self.request.matchdict.get('nameCategory', None)
        parent = Category.by_uid(idcategory)
        if (idcategory != -1 and parent is None) or \
           (parent and parent.name != namecategory):
            return HTTPNotFound()

        form = CategoryForm(self.request.POST, request=self.request)
        if self.request.method == 'POST' and form.validate():
            session = Category.get_session()
            try:
                # pylint: disable=E1101
                with session.begin_nested():
                    category = Category()
                    category.parent = parent
                    # pylint: disable=E1101
                    form.populate_obj(category)
                    session.add(category)
                    session.flush()
                    url = self.request.route_url('view_category',
                                                 idCategory=category.uid,
                                                 nameCategory=category.name)
                    return HTTPFound(url)
            except IntegrityError:
                errors = form.errors.get('name', [])
                errors.append("Nom déjà existant")
                form.errors['name'] = errors

        return {'title': 'Nouvelle categorie',
                'idCategory': idcategory,
                'nameCategory': namecategory,
                'form': form}


    @MenuAdministration(order=2,
                        display='Modifier categorie',
                        route_name=None,
                        route_name_category='edit_category')
    @view_config(route_name='edit_category',
                 renderer='admin/category.mak',
                 permission='write')
    def edit_category(self):
        """
        Display the content of a category
        """
        idcategory = int(self.request.matchdict.get('idCategory', -1))
        namecategory = self.request.matchdict.get('nameCategory', None)
        category = Category.by_uid(idcategory)
        if category is None:
            return HTTPNotFound()

        form = CategoryForm(self.request.POST, category, request=self.request)
        if self.request.method == 'POST' and form.validate():
            session = Category.get_session()
            try:
                # pylint: disable=E1101
                with session.begin_nested():
                    if form.name.data != category.name:
                        category.updateName(form.name.data)
                    # category = Category()
                    # category.parent = parent
                    # pylint: disable=E1101
                    #form.populate_obj(category)
                    #session.add(category)
                    #session.flush()
                    url = self.request.route_url('view_category',
                                                 idCategory=category.uid,
                                                 nameCategory=category.name)
                    return HTTPFound(url)
            except IntegrityError:
                errors = form.errors.get('name', [])
                errors.append("Nom déjà existant")
                form.errors['name'] = errors

        return {'title': 'Modifier la categorie',
                'idCategory': idcategory,
                'nameCategory': namecategory,
                'form': form}
