# coding : utf-8
"""
User forms module
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


class GroupAccessForm(Form):
    groupName = HiddenField()
    access = BooleanField()


class UserForm(CSRFSecureForm):
    login = TextField()
    password = TextField()
    firstname = TextField()
    lastname = TextField()
    email = TextField()
    groups = FieldList(FormField(GroupAccessForm))
