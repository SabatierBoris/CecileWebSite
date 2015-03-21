# vim: set fileencoding=utf-8 :
"""
Item Model module
"""
import os

from pyramid.threadlocal import get_current_registry

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


from . import (
    BASE,
    Dateable,
)


class Item(Dateable, BASE):
    """
    Item model class
    """
    __tablename__ = 'item'
    name = Column(String,
                  nullable=False,
                  info={'trim': True})
    item_type = Column(String(50))
    parent_id = Column(Integer, ForeignKey('category.uid'), nullable=True)
    parent = relationship('Category', foreign_keys=[parent_id])
    __mapper_args__ = {
        'polymorphic_identity': 'item',
        'polymorphic_on': item_type,
    }
    __table_args__ = (UniqueConstraint('name',
                                       'parent_id',
                                       name='item_by_parent'),)

    @property
    def thumbnail(self):
        """
        Get the thumbnail of the item
        """
        raise NotImplementedError("Thumbnail method should be implemented")

    @property
    def thumbnailover(self):
        """
        Get the thumbnailOver of the item
        """
        raise NotImplementedError("ThumbnailOver method should be implemented")

    def is_a_child_of(self, parent):
        """
        Know if self is a child (or sub child) of parent
        """
        if self.parent is None:
            return False
        if self.parent == parent:
            return True
        return self.parent.is_a_child_of(parent)

    @classmethod
    def get_with_direct_parent(cls, parent):
        """
        Get all item with a direct parent
        """
        # pylint: disable=E1101
        cat = cls.get_session().query(Item)
        return cat.filter(Item.parent == parent).all()

    def get_base(self):
        """
        Get the base directory of the category
        """
        settings = get_current_registry().settings
        base = None
        if 'content.dir' in settings:
            base = settings['content.dir']
        if 'content.dir_env' in settings:
            base = os.environ[settings['content.dir_env']]
        if not base:
            raise Exception("content settings not found")
        if self.parent:
            base = self.parent.get_dir()
        return base

    def get_dir(self):
        """
        Get the category directory
        """
        base = self.get_base()
        return os.path.join(base, self.name)
