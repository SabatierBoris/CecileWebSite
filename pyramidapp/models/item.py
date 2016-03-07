# vim: set fileencoding=utf-8 :
"""
Item Model module
"""
import os
import unicodedata

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

    link = relationship('Link', uselist=False, back_populates="item")

    def __init__(self):
        """
        Constructor
        """
        self.do_not_generate = False

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

    def view_url(self,request):
        """
        Get the view url of the item
        """
        raise NotImplementedError("view_url method should be implemented")

    def is_a_child_of(self, parent):
        """
        Know if self is a child (or sub child) of parent
        """
        if self.parent is None:
            return False
        if self.parent == parent:
            return True
        return self.parent.is_a_child_of(parent)

    @property
    def previous(self):
        """
        Get the previous item
        """
        return (self.get_session()
                    .query(Item)
                    .filter(Item.parent_id == self.parent_id)
                    .filter(Item.uid < self.uid)
                    .filter(Item.item_type != 'category')
                    .order_by(Item.uid.desc())
                    .first())

    @property
    def next(self):
        """
        Get the next item
        """
        return (self.get_session()
                    .query(Item)
                    .filter(Item.parent_id == self.parent_id)
                    .filter(Item.uid > self.uid)
                    .filter(Item.item_type != 'category')
                    .order_by(Item.uid)
                    .first())

    @classmethod
    def get_with_direct_parent(cls, parent):
        """
        Get all item with a direct parent
        """
        from pyramidapp.models.category import Category
        # pylint: disable=E1101
        cat = cls.get_session().query(Category).order_by(Item.uid)
        return cat.filter(Category.parent == parent).all()

    def get_base(self):
        """
        Get the base directory of the category
        """
        settings = get_current_registry().settings
        base = None
        if settings['content.dir'] in os.environ:
            base = os.environ[settings['content.dir']]
        else:
            base = settings['content.dir']
        if not base:
            raise Exception("content settings not found")
        if self.parent:
            base = self.parent.get_dir()
        return base

    @classmethod
    def asciify_string(cls, string):
        """
        Return ASCII compliante value of the string
        """
        return unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode('ASCII')

    def get_dir(self):
        """
        Get the category directory
        """
        base = self.get_base()
        return os.path.join(base, self.name)

    def delete(self):
        """
        Delete a item
        """
        session = self.get_session()
        if self.link:
            self.link.delete()
        session.delete(self)
        self.do_not_generate=True
        if self.thumbnail and os.path.isfile(self.thumbnail):
            os.remove(self.thumbnail)
        if self.thumbnailover and os.path.isfile(self.thumbnailover):
            os.remove(self.thumbnailover)
        session.commit()
        try:
            super().delete()
        except:
            pass
