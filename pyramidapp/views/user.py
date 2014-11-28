"""
The user view part
"""
from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound,
)

from ..forms.user import UserForm

from ..models.user import User, UserGroupAccess
from ..models.group import Group


class UserView(object):
    """
    The user view logic
    """
    def __init__(self, request):
        self.request = request

    @view_config(route_name='user_list',
                 renderer='admin/userList.mak',
                 permission='admin')
    @view_config(route_name='user_list:new',
                 renderer='admin/userList.mak',
                 permission='admin')
    def user_list(self):
        """
        Get the list of all users
        """
        new = self.request.matchdict.get('new', False)
        if new:
            new = True

        user_list = User.all()
        group_list = Group.all()
        forms = []
        if new:
            user_list.append(User())

        for user in user_list:
            forms.append(UserForm(self.request.POST, UserGroupAccess(user),
                                  prefix=user.login, request=self.request))

        if self.request.method == 'POST':
            error = False
            for k, user in enumerate(user_list):
                if forms[k].validate():
                    forms[k].populate_obj(UserGroupAccess(user))
                    if user.uid is None:
                        # pylint: disable=E1101
                        User.get_session().add(user)
                else:
                    error = True
            if not error:
                # pylint: disable=E1101
                User.get_session().commit()
                return HTTPFound(location=self.request.route_url('user_list'))

        return {'title': 'Liste des utilisateurs',
                'user_list': user_list,
                'group_list': group_list,
                'forms': forms}

    @view_config(route_name='user_delete')
    def user_delete(self):
        """
        Delete a user
        """
        uid = int(self.request.matchdict.get('uid', -1))
        entry = User.by_uid(uid)
        if entry:
            # pylint: disable=E1101
            User.get_session().delete(entry)
            User.get_session().commit()
        return HTTPFound(location=self.request.route_url('user_list'))
