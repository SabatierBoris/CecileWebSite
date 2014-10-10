# coding : utf-8
"""
Right forms module
"""
from .csrfform import CSRFSecureForm
from wtforms.fields import (
    TextField,
)


class RightForm(CSRFSecureForm):
    """
    Form for right edition
    """
    name = TextField()
