# coding : utf-8
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
    """
    Form for editing group
    """
    name = TextField()
    rights = FieldList(FormField(RightAccessForm))
