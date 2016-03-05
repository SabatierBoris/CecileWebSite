# vim: set fileencoding=utf-8 :
"""
The user view part
"""
from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound,
)
from sqlalchemy.exc import IntegrityError

from pyramidapp.models.tag import Tag
from pyramidapp.models.menu import MenuAdministration
from pyramidapp.models.user import User, UserGroupAccess
from pyramidapp.models.group import Group
from pyramidapp.forms.user import UserForm


class UserView(object):
    """
    The user view logic
    """
    def __init__(self, request):
        self.request = request

    @MenuAdministration(order=22,
                        display='Gestion des utilisateurs',
                        route_name='user_list')
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
            session = User.get_session()
            for k, user in enumerate(user_list):
                try:
                    # pylint: disable=E1101
                    with session.begin_nested():
                        if forms[k].validate():
                            forms[k].populate_obj(UserGroupAccess(user))
                            if user.uid is None:
                                # pylint: disable=E1101
                                session.add(user)
                        else:
                            error = True
                    session.commit()
                except IntegrityError:
                    errors = forms[k].errors.get('login', [])
                    errors.append("Login déjà existant")
                    forms[k].errors['login'] = errors
                    error = True
            if not error:
                # pylint: disable=E1101
                return HTTPFound(location=self.request.route_url('user_list'))

        return {'tags' : Tag.all(),
                'title': 'Liste des utilisateurs',
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
