# coding : utf-8
"""
Right forms module
"""
from wtforms_alchemy import ModelForm
from .csrfform import CSRFSecureForm

from ..models.right import Right


class RightForm(ModelForm, CSRFSecureForm):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    Right form
    """
    class Meta:
        # pylint: disable=R0903,W0232
        #    Too fee pyblic methods: we are juste a model
        """
        Meta class of the right form
        """
        model = Right

    @classmethod
    def get_session(cls):
        """
        Get the sqlalchemy session
        """
        return Right.get_session()
