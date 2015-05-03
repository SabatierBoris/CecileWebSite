# vim: set fileencoding=utf-8 :
"""
The item view part
"""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from pyramid.response import FileResponse

from pyramidapp.models.item import Item


class ItemView(object):
    """
    The item view logic
    """
    def __init__(self, request):
        self.request = request

    @view_config(route_name='thumbnail')
    def view_thumbnail(self):
        """
        Display the thumbnail of a item
        """
        iditem = int(self.request.matchdict.get('idItem', -1))
        nameitem = self.request.matchdict.get('nameItem', '')

        item = Item.by_uid(iditem)

        if item is None or item.name != nameitem:
            return HTTPNotFound("Item %s-%s not found", iditem, nameitem)

        thumb = item.thumbnail

        response = FileResponse(thumb,
                                request=self.request,
                                content_type='image/jpeg')
        return response

    @view_config(route_name='thumbnail_over')
    def view_thumbnail_over(self):
        """
        Display the thumbnail_over of a item
        """
        iditem = int(self.request.matchdict.get('idItem', -1))
        nameitem = self.request.matchdict.get('nameItem', '')

        item = Item.by_uid(iditem)

        if item is None or item.name != nameitem:
            return HTTPNotFound("Item %s-%s not found", iditem, nameitem)

        thumb = item.thumbnailover

        response = FileResponse(thumb,
                                request=self.request,
                                content_type='image/jpeg')
        return response
