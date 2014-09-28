# coding : utf-8
"""
Group forms module
"""

from wtforms import Form
from wtforms.fields import (
    BooleanField,
    TextField,
    FieldList,
    FormField,
    HiddenField,
)
from wtforms_alchemy import ModelForm

from .csrfform import CSRFSecureForm

from ..models.group import Group


class RightAccessForm(Form):
    rightName = HiddenField()
    access = BooleanField()


class GroupForm(CSRFSecureForm):
    name = TextField()
    rights = FieldList(FormField(RightAccessForm))
