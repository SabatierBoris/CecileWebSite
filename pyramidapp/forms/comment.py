# vim: set fileencoding=utf-8 :
"""
Right forms module
"""
from .csrfform import CSRFSecureForm
from wtforms.fields import (
    TextField,
    TextAreaField,
)
from wtforms import validators


class CommentForm(CSRFSecureForm):
    # pylint: disable=R0903
    """
    Form for comment edition
    """
    name = TextField(u'Pseudo : ', validators=[validators.required("Nom obligatoire")])
    comment = TextAreaField(u'Commentaire : ', validators=[validators.required("Texte obligatoire")])
