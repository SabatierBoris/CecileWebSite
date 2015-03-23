# vim: set fileencoding=utf-8 :
"""
Picture Model module
"""
import os

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

import imghdr

from . import (
    BASE,
)

from pyramidapp.models.item import Item
from pyramidapp.models.tag import TaggableItem
from pyramidapp.models.image import generate_thumbnail, generate_thumbnail_over


class Picture(Item, TaggableItem, BASE):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    Picture Model
    """
    __tablename__ = 'picture'
    uid = Column(Integer, ForeignKey('item.uid'), primary_key=True)
    original_image_name = Column(String)
    __mapper_args__ = {
        'polymorphic_identity': 'picture',
    }

    @property
    def thumbnail(self):
        """
        Get the thumbnail of the item
        """
        thumbnail = os.path.join(self.get_dir(), "thumbnail_%s.png"%(os.path.basename(self.original_image_name)))
        if not os.path.isfile(thumbnail):
            generate_thumbnail(self.original_image_name, thumbnail)
        return thumbnail

    @property
    def thumbnailover(self):
        """
        Get the thumbnailOver of the item
        """
        thumbnail = os.path.join(self.get_dir(), "thumbnail_over_%s.png"%(os.path.basename(self.original_image_name)))
        if not os.path.isfile(thumbnail):
            generate_thumbnail_over(self.original_image_name,
                                    thumbnail,
                                    self.name.upper())
        return thumbnail

    @property
    def image(self):
        """
        Get the image of the item
        """
        self = self

    @image.setter
    def image(self, val):
        """
        Set the image of the item
        """
        val.file.seek(0)
        ext = imghdr.what('unused', val.file.read())
        val.file.seek(0)
        path = os.path.join(self.get_dir(), "Picture_original_%s.%s" % (self.name,ext))
        self.original_image_name = path
        output_file = open(path, 'wb')

        while not val.file.closed:
            data = val.file.read(2 << 16)
            if not data:
                val.file.close()
            output_file.write(data)
        output_file.close()

    def get_dir(self):
        """
        Get the category directory
        """
        return self.get_base()
