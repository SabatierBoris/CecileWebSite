# coding : utf-8
"""
Access Model module
"""
from sqlalchemy import (
    Column,
    Integer,
    String,
)

from . import BASE


class Access(BASE):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    Access Model
    """
    __tablename__ = 'access'
    uid = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __init__(self, name):
        super(Access, self).__init__()
        self.name = name
