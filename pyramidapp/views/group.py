# vim: set fileencoding=utf-8 :
"""
The group view part
"""
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from sqlalchemy.exc import IntegrityError

from pyramidapp.models.tag import Tag
from pyramidapp.models.menu import MenuAdministration
from pyramidapp.models.group import Group, GroupRightAccess
from pyramidapp.models.right import Right

from pyramidapp.forms.group import GroupForm


class GroupView(object):
    """
    The group view logic
    """
    def __init__(self, request):
        self.request = request

    @MenuAdministration(order=21,
                        display='Gestion des groupes',
                        route_name='group_list')
    @view_config(route_name='group_list',
                 renderer='admin/groupList.mak',
                 permission='admin')
    @view_config(route_name='group_list:new',
                 renderer='admin/groupList.mak',
                 permission='admin')
    def group_list(self):
        """
        Get the list of all groups
        """
        new = self.request.matchdict.get('new', False)
        if new:
            new = True
        forms = []
        group_list = Group.all()
        right_list = Right.all()
        if new:
            group_list.append(Group())

        for group in group_list:
            forms.append(GroupForm(self.request.POST, GroupRightAccess(group),
                                   prefix=group.name, request=self.request))

        if self.request.method == 'POST':
            error = False
            session = Group.get_session()
            for k, group in enumerate(group_list):
                try:
                    # pylint: disable=E1101
                    with session.begin_nested():
                        if forms[k].validate():
                            forms[k].populate_obj(GroupRightAccess(group))
                            if group.uid is None:
                                # pylint: disable=E1101
                                session.add(group)
                        else:
                            error = True
                    session.commit()
                except IntegrityError:
                    msg = "Nom déjà existant"
                    errors = forms[k].errors.get('name', [])
                    errors.append(msg)
                    forms[k].errors['name'] = errors
                    error = True
            if not error:
                # pylint: disable=E1101
                return HTTPFound(location=self.request.route_url('group_list'))

        return {'tags' : Tag.all(),
                'title': 'Liste des groupes',
                'right_list': right_list,
                'group_list': group_list,
                'forms': forms}

    @view_config(route_name='group_delete', permission='admin')
    def group_delete(self):
        """
        Delete a group
        """
        uid = int(self.request.matchdict.get('uid', -1))
        entry = Group.by_uid(uid)
        if entry:
            # pylint: disable=E1101
            Group.get_session().delete(entry)
            Group.get_session().commit()
        return HTTPFound(location=self.request.route_url('group_list'))
