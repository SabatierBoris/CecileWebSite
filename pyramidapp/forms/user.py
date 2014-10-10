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

from .csrfform import CSRFSecureForm


class GroupAccessForm(Form):
    # pylint: disable=R0903
    #    Too few pyblic methods: we are juste a model
    """
    Subform for access a group to a user
    """
    groupName = HiddenField()
    access = BooleanField()


class UserForm(CSRFSecureForm):
    """
    Form for user edition
    """
    login = TextField()
    password = TextField()
    firstname = TextField()
    lastname = TextField()
    email = TextField()
    groups = FieldList(FormField(GroupAccessForm))
