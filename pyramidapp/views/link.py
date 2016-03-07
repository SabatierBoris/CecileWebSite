# vim: set fileencoding=utf-8 :
"""
The Link view part
"""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.response import FileResponse

from sqlalchemy.exc import IntegrityError

from pyramidapp.models.menu import MenuAdministration
from pyramidapp.models.item import Item
from pyramidapp.models.picture import Picture
from pyramidapp.models.link import Link
from pyramidapp.models.tag import Tag

from pyramidapp.forms.link import LinkForm

class LinkView(object):
    """
    The link view logic
    """
    def __init__(self, request):
        self.request = request

    @MenuAdministration(order=7,
                        display='Gestion du lien',
                        route_name=None,
                        route_name_for_item='new_link',
                        cls=Picture)
    @view_config(route_name='new_link',
                 renderer='admin/link.mak',
                 permission='write')
    def new_link(self):
        """
        Display the link form for an item
        """
        iditem = int(self.request.matchdict.get('idItem', -1))
        nameitem = self.request.matchdict.get('nameItem', None)
        item = Item.by_uid(iditem)
        if item is None:
            return HTTPNotFound()

        if item.link != None:
            form = LinkForm(self.request.POST, request=self.request, obj=item.link)
        else:
            form = LinkForm(self.request.POST, request=self.request)
        if self.request.method == 'POST' and form.validate():
            session = Picture.get_session()
            try:
                # pylint: disable=E1101
                with session.begin_nested():
                    if item.link != None:
                        link = item.link
                    else:
                        link = Link()
                        link.item = item
                    # pylint: disable=E1101
                    form.populate_obj(link)
                    if item.uid is None:
                        # pylint: disable=E1101
                        session.add(link)
                    session.flush()
                session.commit()

                url = item.view_url(self.request)
                return HTTPFound(url)
            except IntegrityError:
                errors = form.errors.get('name', [])
                errors.append("Nom déjà existant")
                form.errors['name'] = errors
        return {'tags' : Tag.all(),
                'title': 'Nouveau Lien',
                'idItem': iditem,
                'item': item,
                'form': form}

    @view_config(route_name='delete_link',
                 permission='write')
    def delete_link(self):
        """
        Delete a link
        """
        idlink = int(self.request.matchdict.get('idLink', -1))
        link = Link.by_uid(idlink)
        if link is None:
            return HTTPNotFound()
        url = link.item.view_url(self.request)
        link.delete()
        return HTTPFound(url)
