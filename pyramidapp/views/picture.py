# vim: set fileencoding=utf-8 :
"""
The picture view part
"""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.response import FileResponse

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

    @view_config(route_name='original_picture')
    def view_original_picture(self):
        """
        Display the original picutre
        """
        idpicture = int(self.request.matchdict.get('idItem', -1))
        namepicture = self.request.matchdict.get('nameItem', '')
        picture = Picture.by_uid(idpicture)

        if picture is None or picture.name != namepicture:
            return HTTPNotFound("Picture %d-%s not found", idpicture, namepicture)

        response = FileResponse(picture.original_image_name,
                                request=self.request,
                                content_type='image/jpeg')
        return response

    @view_config(route_name='view_picture',
                 renderer='picture.mak')
    def view_picture(self):
        """
        Display a picture
        """
        idpicture = int(self.request.matchdict.get('idItem', -1))
        namepicture = self.request.matchdict.get('nameItem', None)
        picture = Picture.by_uid(idpicture)
        if picture is None or picture.name != namepicture:
            return HTTPNotFound()

        return {'item': picture,
                'idCategory': picture.parent.uid}


    @MenuAdministration(order=4,
                        display='Nouvelle image',
                        route_name=None,
                        route_name_for_item='new_picture',
                        cls=Category)
    @view_config(route_name='new_picture',
                 renderer='admin/picture.mak',
                 permission='write')
    def new_picture(self):
        """
        Display the content of a category
        """
        idcategory = int(self.request.matchdict.get('idItem', -1))
        namecategory = self.request.matchdict.get('nameItem', None)
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
                session.commit()
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
                'item': parent,
                'form': form}
#
    @MenuAdministration(order=5,
                        display='Supprimer image',
                        route_name=None,
                        route_name_for_item='delete_picture',
                        cls=Picture)
    @view_config(route_name='delete_picture', permission='write')
    def delete_picture(self):
        """
        Remove a picture
        """
        idpicture = int(self.request.matchdict.get('idItem', -1))
        namepicture = self.request.matchdict.get('nameItem', None)
        picture = Picture.by_uid(idpicture)
        if picture is None or picture.name != namepicture:
            return HTTPNotFound()

        if picture.parent != None:
            url = self.request.route_url('view_category',
                                         idItem=picture.parent.uid,
                                         nameItem=picture.parent.name)
        else:
            url = self.request.route_url('home')

        picture.delete()

        return HTTPFound(url)
