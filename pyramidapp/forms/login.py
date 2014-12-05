# vim: set fileencoding=utf-8 :
"""
Login forms module
"""
from .csrfform import CSRFSecureForm
from wtforms.fields import (
    TextField,
    PasswordField,
)
from wtforms import validators


class LoginForm(CSRFSecureForm):
    # pylint: disable=R0903
    """
    Form for login a user
    """
    login = TextField('login', [validators.required("Login obligatoire")])
    password = PasswordField('password',
                             [validators.required("Password obligatoire")])
    errors = {}
