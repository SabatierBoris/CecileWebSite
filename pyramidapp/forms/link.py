# vim: set fileencoding=utf-8 :
"""
Link forms module
"""
from .csrfform import CSRFSecureForm
from wtforms.fields import (
    TextField,
)
from wtforms import validators


class LinkForm(CSRFSecureForm):
    # pylint: disable=R0903
    """
    Form for link edition
    """
    name = TextField(validators=[validators.required("Nom obligatoire")])
    link = TextField(validators=[validators.required("URL obligatoire")])
