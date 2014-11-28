"""
The login/logout view part
"""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPForbidden
from pyramid.security import remember
from pyramid.security import forget

from pyramidapp.forms.login import LoginForm
from pyramidapp.models.user import User


class LoginView(object):
    """
    The login/logout view logic
    """
    def __init__(self, request):
        self.request = request

    @view_config(context=HTTPForbidden, renderer='login.mak')
    @view_config(route_name='login', renderer='login.mak')
    def login(self):
        """
        The login logic
        """
        login_url = self.request.route_url('login')
        referer = self.request.url
        if referer == login_url:
            referer = self.request.route_url('home')

        form = LoginForm(self.request.POST, request=self.request)

        if self.request.method == 'POST':
            if form.validate():
                use = User.by_login_password(form.login.data,
                                             form.password.data)
                if use is not None:
                    headers = remember(self.request, use.login)
                    return HTTPFound(location=referer, headers=headers)
                else:
                    form.errors['user'] = 'Login ou Password incorrect'
        return {'title': 'Connexion', 'form': form}

    @view_config(route_name="logout")
    def logout(self):
        """
        The logout logic
        """
        headers = forget(self.request)
        return HTTPFound(location=self.request.route_url('home'),
                         headers=headers)
