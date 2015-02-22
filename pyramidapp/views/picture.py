# vim: set fileencoding=utf-8 :
"""
The picture view part
"""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from sqlalchemy.exc import IntegrityError

from pyramidapp.models.menu import MenuAdministration
from pyramidapp.models.category import Category
from pyramidapp.models.picture import Picture
from pyramidapp.forms.picture import PictureForm


class PictureView(object):
    """
    The picture view logic
    """
    def __init__(self, request):
        self.request = request


    @MenuAdministration(order=3,
                        display='Nouvelle image',
                        route_name=None,
                        route_name_category='new_picture')
    @view_config(route_name='new_picture',
                 renderer='admin/picture.mak',
                 permission='write')
    def new_picture(self):
        """
        Display the content of a category
        """
        idcategory = int(self.request.matchdict.get('idCategory', -1))
        namecategory = self.request.matchdict.get('nameCategory', None)
        parent = Category.by_uid(idcategory)
        if parent is None:
            return HTTPNotFound()

        form = PictureForm(self.request.POST, request=self.request)

        if self.request.method == 'POST' and form.validate():
            session = Picture.get_session()
            try:
                # pylint: disable=E1101
                with session.begin_nested():
                    picture = Picture()
                    picture.parent = parent
                    # pylint: disable=E1101
                    form.populate_obj(picture)
                    session.add(picture)
                    session.flush()
                    url = self.request.route_url('view_category',
                                                 idCategory=parent.uid,
                                                 nameCategory=parent.name)
                    return HTTPFound(url)
            except IntegrityError:
                errors = form.errors.get('name', [])
                errors.append("Nom déjà existant")
                form.errors['name'] = errors

        return {'title': 'Nouvelle Image',
                'idCategory': idcategory,
                'nameCategory': namecategory,
                'form': form}
