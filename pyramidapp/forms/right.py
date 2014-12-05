# vim: set fileencoding=utf-8 :
"""
Right forms module
"""
from .csrfform import CSRFSecureForm
from wtforms.fields import (
    TextField,
)


class RightForm(CSRFSecureForm):
    # pylint: disable=R0903
    """
    Form for right edition
    """
    name = TextField()
