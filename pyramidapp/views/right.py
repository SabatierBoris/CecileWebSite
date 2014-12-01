"""
The right view part
"""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from pyramidapp.models.menu import MenuAdministration
from ..models.right import Right
from ..forms.right import RightForm


class RightView(object):
    """
    The right view logic
    """
    def __init__(self, request):
        self.request = request

    @MenuAdministration(order=20,
                        display='Gestion des droits',
                        route_name='right_list',
                        route_name_category=None)
    @view_config(route_name='right_list',
                 renderer='admin/rightList.mak',
                 permission='admin')
    @view_config(route_name='right_list:new',
                 renderer='admin/rightList.mak',
                 permission='admin')
    def right_list(self):
        """
        Get the list of all right
        """
        new = self.request.matchdict.get('new', False)
        if new:
            new = True

        forms = []

        right_list = Right.all()
        if new:
            right_list.append(Right())

        for k, right in enumerate(right_list):
            # pylint: disable=E1123
            forms.append(RightForm(self.request.POST, right,
                                   prefix=right.name, request=self.request))

        if self.request.method == 'POST':
            error = False
            for k, right in enumerate(right_list):
                if forms[k].name.data != right.name:
                    if forms[k].validate():
                        forms[k].populate_obj(right)
                        if right.uid is None:
                            # pylint: disable=E1101
                            Right.get_session().add(right)
                    else:
                        error = True
            if not error:
                # pylint: disable=E1101
                Right.get_session().commit()
                return HTTPFound(location=self.request.route_url('right_list'))

        return {'title': 'Liste des droits',
                'right_list': right_list,
                'forms': forms}

    @view_config(route_name='right_delete', permission='admin')
    def right_delete(self):
        """
        Delete a right
        """
        uid = int(self.request.matchdict.get('uid', -1))
        entry = Right.by_uid(uid)
        if entry:
            # pylint: disable=E1101
            Right.get_session().delete(entry)
            Right.get_session().commit()
        return HTTPFound(location=self.request.route_url('right_list'))
