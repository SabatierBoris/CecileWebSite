# coding : utf-8
"""
Category Model module
"""

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import backref, relationship

from . import (
    DB_SESSION,
    BASE,
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
    parent_id = Column(Integer,
                       ForeignKey('category.uid'))
    name = Column(String,
                  unique=True,
                  nullable=False,
                  info={'trim': True})
    parent = relationship("Category", remote_side=[uid])
    children = relationship("Category",
                            backref=backref('category', remote_side=[uid]))

    @classmethod
    def all(cls):
        """
        Get all category
        """
        # pylint: disable=E1101
        return DB_SESSION.query(Category).all()

    @classmethod
    def by_uid(cls, uid):
        """
        Get a category with the uid
        """
        # pylint: disable=E1101
        return DB_SESSION.query(Category).filter(Category.uid == uid).first()

    @classmethod
    def get_session(cls):
        """
        Get the sqlalchemy session
        """
        return DB_SESSION
