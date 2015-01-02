# vim: set fileencoding=utf-8 :
"""
Group forms module
"""

from wtforms import Form
from wtforms.fields import (
    TextField,
    BooleanField,
    FormField,
    FieldList,
    HiddenField,
)
from wtforms import validators

from .csrfform import CSRFSecureForm


class RightAccessForm(Form):
    # pylint: disable=R0903
    #    Too few pyblic methods: we are juste a model
    """
    Subform for access a right to a group
    """
    rightName = HiddenField()
    access = BooleanField()


class GroupForm(CSRFSecureForm):
    # pylint: disable=R0903
    """
    Form for editing group
    """
    name = TextField(validators=[validators.required("Nom obligatoire")])
    rights = FieldList(FormField(RightAccessForm))
