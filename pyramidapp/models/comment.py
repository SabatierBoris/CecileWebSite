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
from sqlalchemy.orm import relationship
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


ASSOCIATION_TABLE = Table('item_comment', BASE.metadata,
                          Column('comment_id', Integer, ForeignKey(Comment.uid)),
                          Column('item_id', Integer, ForeignKey(Item.uid)))


class CommentableItem(object):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a builtin
    """
    Builtin class for add the tags attribute to items
    """
    @staticmethod
    @declared_attr
    def comments():
        """
        Attribute to get the comments of an item
        """
        return relationship('Comment',
                            secondary='item_comment',
                            backref='items')
