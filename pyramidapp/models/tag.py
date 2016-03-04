# vim: set fileencoding=utf-8 :
"""
Tag Model module
"""
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import as_declarative, declared_attr, AbstractConcreteBase

from . import (
    BASE,
    Dateable,
)
from pyramidapp.models.item import Item

ASSOCIATION_TABLE = Table('item_tag', BASE.metadata,
                          Column('tag_id', Integer, ForeignKey("tag.uid")),
                          Column('item_id', Integer, ForeignKey(Item.uid)))


class Tag(Dateable, BASE):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    Tag model class
    """
    __tablename__ = 'tag'
    name = Column(String,
                  nullable=False,
                  unique=True,
                  info={'trim': True})
    items = relationship("Item", secondary=ASSOCIATION_TABLE)

    @classmethod
    def by_name(cls, name):
        """
        Get a tag by the tag name
        """
        # pylint: disable=E1101
        return cls.get_session().query(cls).filter(cls.name == name).first()

    def delete(self):
        session = self.get_session()
        session.delete(self)
        session.commit()


class TaggableItem(AbstractConcreteBase):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a builtin
    """
    Builtin class for add the tags attribute to items
    """
    @declared_attr
    def tags(cls):
        return relationship('Tag',
                            secondary='item_tag')

    def delete(self):
        for t in self.tags:
            if len(t.items) == 0:
                t.delete()
