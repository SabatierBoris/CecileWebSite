# vim: set fileencoding=utf-8 :
"""
Validators module
"""
from wtforms.validators import ValidationError
import imghdr


class ImageFileRequired(object):
    # pylint: disable=R0903
    """
    Validates that an uploaded file from a FileField is an image.
    Better than checking the file extention, examines the header
    of the image using Python's built in imghdr module.
    """
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        if field.data is None or field.data == b'':
            message = self.message or 'An image file is required'
            raise ValidationError(message)
        field.data.file.seek(0)
        ext = imghdr.what('unused', field.data.file.read())
        if ext is None:
            message = self.message or 'An image file is required'
            raise ValidationError(message)
        field.data.file.seek(0)

