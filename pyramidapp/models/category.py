# vim: set fileencoding=utf-8 :
"""
Category Model module
"""
import os

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy import event

import imghdr

from sqlalchemy.orm import backref, relationship

from pyramidapp.models.item import Item
from pyramidapp.models.image import generate_thumbnail, generate_thumbnail_over


class Category(Item):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    Category Model
    """
    __tablename__ = 'category'
    uid = Column(Integer,
                 ForeignKey('item.uid',
                            use_alter=True,
                            name='fk_category_item'),
                 primary_key=True)
    original_image_name = Column(String)
    __mapper_args__ = {
        'inherit_condition': (uid == Item.uid),
        'polymorphic_identity': 'category'
    }
    children = relationship("Item",
                            backref=backref('category'),
                            foreign_keys=[Item.parent_id])

    def updateName(self, value):
        thumb = self.thumbnail
        thumbover = self.thumbnailover
        original = self.original_image_name
        _, ext = os.path.splitext(original)
        for image in [thumb, thumbover]:
            if os.path.isfile(image):
                os.remove(image)
        self.name = value
        newOriginal = self.getOriginalImageName(ext)
        os.rename(original, newOriginal)
        self.original_image_name = newOriginal

    def get_content(self):
        """
        Get the content of the category
        """
        for child in self.children:
            yield child

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

    def view_url(self,request):
        """
        Get the view url of the item
        """
        return request.route_url('view_category',idCategory=self.uid,nameCategory=self.name)

    @thumbnail.setter
    def thumbnail(self, val):
        """
        Set the thumbnail of the item
        """
        val.file.seek(0)
        ext = imghdr.what('unused', val.file.read())
        val.file.seek(0)
        path = self.getOriginalImageName(ext)
        self.original_image_name = path
        output_file = open(path, 'wb')

        while not val.file.closed:
            data = val.file.read(2 << 16)
            if not data:
                val.file.close()
            output_file.write(data)
        output_file.close()

    def getOriginalImageName(self, ext):
        return os.path.join(self.get_dir(), "Category_original_%s.%s" % (self.name,ext))


@event.listens_for(Category.name, 'set')
def create_category_dir(target, value, oldvalue, initiator):
    """
    Create of move the category directory
    """
    initiator = initiator
    base = target.get_base()
    new_dir = os.path.join(base, value)
    if not oldvalue:
        old_dir = os.path.join(base, oldvalue)
        os.renames(old_dir, new_dir)
    else:
        try:
            os.makedirs(new_dir)
        except os.error:
            pass
