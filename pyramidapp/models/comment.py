# vim: set fileencoding=utf-8 :
"""
Comment Model module
"""
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr

from . import (
    BASE,
    Dateable,
)
from pyramidapp.models.item import Item


class Comment(Dateable, BASE):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    Comment model class
    """
    __tablename__ = 'comment'
    name = Column(String,
                  nullable=False,
                  info={'trim': True})
    comment = Column(Text, nullable=False)
    item_id = Column(Integer, ForeignKey('item.uid'), nullable=False)
    item = relationship('Item', foreign_keys=[item_id])

    valid = Column(Boolean, unique=False, default=False, nullable=False)

    parent_id = Column(Integer, ForeignKey('comment.uid'), nullable=True)
    children = relationship('Comment',
                            cascade="all",
                            backref=backref('parent', remote_side='Comment.uid'))

    @classmethod
    def get_waiting_for_validation(cls):
        """
        Get all comment in waiting for validation
        """
        cat = cls.get_session().query(Comment)
        return cat.filter(Comment.valid == False).all()


class CommentableItem(object):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a builtin
    """
    Builtin class for add the tags attribute to items
    """
    @declared_attr
    def comments(self):
        """
        Attribute to get the comments of an item
        """
        return relationship('Comment', lazy='dynamic')
