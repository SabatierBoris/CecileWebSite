# coding : utf-8
"""
Group Model module
"""
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import relationship

from . import BASE
from .access import Access


class Group(BASE):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    Group Model
    """
    __tablename__ = 'group'
    uid = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    access = relationship('Access', secondary='group_access', backref='groups')

    def __init__(self, name):
        super(Group, self).__init__()
        self.name = name

ASSOCIATION_TABLE = Table('group_access', BASE.metadata,
                          Column('group_id', Integer, ForeignKey(Group.uid)),
                          Column('access_id', Integer, ForeignKey(Access.uid)))
