# vim: set fileencoding=utf-8 :
"""
Category forms module
"""
from .csrfform import CSRFSecureForm
from wtforms.fields import (
    TextField,
    FileField,
)
from wtforms.validators import Required

from pyramidapp.forms.validators import ImageFileRequired


class CategoryForm(CSRFSecureForm):
    # pylint: disable=R0903
    """
    Form for category edition
    """
    name = TextField(u'Nom', [Required()])
    thumbnail = FileField(u'Miniature', [ImageFileRequired()])
