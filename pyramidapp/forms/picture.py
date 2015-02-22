# vim: set fileencoding=utf-8 :
"""
Picture forms module
"""
from .csrfform import CSRFSecureForm
from wtforms.fields import (
    TextField,
    FileField,
)
from wtforms.validators import Required

from pyramidapp.forms.validators import ImageFileRequired


class PictureForm(CSRFSecureForm):
    # pylint: disable=R0903
    """
    Form for picture edition
    """
    name = TextField(u'Nom', [Required()])
    image = FileField(u'Image', [ImageFileRequired()])

