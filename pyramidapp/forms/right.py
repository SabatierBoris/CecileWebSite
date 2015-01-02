# vim: set fileencoding=utf-8 :
"""
Right forms module
"""
from .csrfform import CSRFSecureForm
from wtforms.fields import (
    TextField,
)
from wtforms import validators


class RightForm(CSRFSecureForm):
    # pylint: disable=R0903
    """
    Form for right edition
    """
    name = TextField(validators=[validators.required("Nom obligatoire")])

