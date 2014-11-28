# coding : utf-8
"""
Category Model module
"""

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

from . import (
    BASE,
    DB_SESSION,
    Dateable,
)


class Category(BASE, Dateable):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    Category Model
    """
    __tablename__ = 'category'
    uid = Column(Integer, primary_key=True)
    name = Column(String,
                  unique=True,
                  nullable=False,
                  info={'trim': True})
    parent_id = Column(Integer,
                       ForeignKey('category.uid'))
    parent = relationship("Category", remote_side=[uid])
    children = relationship("Category",
                            backref=backref('category',remote_side=[uid]))
