# coding : utf-8
"""
Category forms module
"""
from .csrfform import CSRFSecureForm
from wtforms.fields import (
    TextField,
)


class CategoryForm(CSRFSecureForm):
    # pylint: disable=R0903
    """
    Form for category edition
    """
    name = TextField()
