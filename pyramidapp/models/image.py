# vim: set fileencoding=utf-8 :
"""
Image manipulation module
"""
import os

from pyramid.threadlocal import get_current_registry

from PIL import Image, ImageFont, ImageFilter, ImageDraw, ImageChops

from itertools import product


THUMBNAIL_BLUR = 2
THUMBNAIL_SHADOW_COLOR = (255, 255, 255)
THUMBNAIL_SHADOW_INFO = (0, 1)
THUMBNAIL_TEXT_COLOR = (0, 0, 0)
THUMBNAIL_SIZE = (400, 300)
THUMBNAIL_POLICE = "pyramidapp/static/fonts/OxygenMono-Regular.otf"
THUMBNAIL_BACKGROUND = (0, 0, 0, 0)


def calcul_full_size_text_police(size, text, police_name):
    """
    Get the police size for the text fit in size
    """
    police_size = 15
    font = ImageFont.truetype(police_name, police_size)
    current_size = font.getsize(text)

    ratio_width = (police_size*size[0])/current_size[0]
    ratio_height = (police_size*size[1])/current_size[1]
    return int(min(ratio_width, ratio_height))


def add_centered_blured_shadow(image, text, police_info,
                               color, shadow_info=(4, 1)):
    """
    Add the shadow of a text in center
    """
    police_name, police_size = police_info
    blur, shift = shadow_info
    tmp_im = Image.new('RGBA', image.size, (color[0], color[1], color[2], 0))
    draw = ImageDraw.Draw(tmp_im)
    font = ImageFont.truetype(police_name, police_size)
    text_size = font.getsize(text)
    # Correct the inclution of the offset in getsize
    offset = font.getoffset(text)
    text_size = (text_size[0]+offset[0], text_size[1]+offset[1])

    for shift in product((-shift, 0, shift), repeat=2):
        text_position = (int((image.size[0]-text_size[0])/2)+shift[0],
                         int((image.size[1]-text_size[1])/2)+shift[1])
        draw.text(text_position, text, font=font, fill=color)

    tmp_im = tmp_im.filter(ImageFilter.GaussianBlur(radius=blur))

    return Image.composite(image, tmp_im, ImageChops.invert(tmp_im))


def add_centered_text(image, text, police_name, police_size, color):
    """
    Add a text in center of image
    """
    working_im = image.copy()
    draw = ImageDraw.Draw(working_im)

    font = ImageFont.truetype(police_name, police_size)
    text_size = font.getsize(text)
    # Correct the inclution of the offset in getsize
    offset = font.getoffset(text)
    text_size = (text_size[0]+offset[0], text_size[1]+offset[1])

    text_position = (int((image.size[0]-text_size[0])/2),
                     int((image.size[1]-text_size[1])/2))
    draw.text(text_position, text, font=font, fill=color)

    return working_im


def generate_thumbnail(original, target):
    """
    Generate the thumbnail
    """
    image = Image.open(original)
    image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
    thumbnail = Image.new('RGBA', THUMBNAIL_SIZE, THUMBNAIL_BACKGROUND)

    offset = (int((thumbnail.size[0]-image.size[0])/2),
              int((thumbnail.size[1]-image.size[1])/2))
    thumbnail.paste(image, offset)
    thumbnail.save(target, "JPEG", quality=80, optimize=True, progressive=True)


def generate_thumbnail_over(original, target, text, blur=True):
    """
    Generate the thumbnail in grayscale with the text over
    """
    settings = get_current_registry().settings
    base = None
    if settings['app.dir'] in os.environ:
        base = os.environ[settings['app.dir']]
    else:
        base = settings['app.dir']
    police = "%s%s"%(base,THUMBNAIL_POLICE)
    image = Image.open(original)
    image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
    thumbnail = Image.new('RGBA', THUMBNAIL_SIZE, THUMBNAIL_BACKGROUND)

    image1 = image.convert('L')
    if blur:
        image1 = image1.filter(ImageFilter.GaussianBlur(radius=THUMBNAIL_BLUR))
    if text:
        police_size = calcul_full_size_text_police(image.size,
                                                   text,
                                                   police)
        image1 = add_centered_blured_shadow(image1,
                                            text,
                                            (police, police_size),
                                            THUMBNAIL_SHADOW_COLOR,
                                            THUMBNAIL_SHADOW_INFO)
        image1 = add_centered_text(image1,
                                   text,
                                   police,
                                   police_size,
                                   THUMBNAIL_TEXT_COLOR)

    offset = (int((thumbnail.size[0]-image1.size[0])/2),
              int((thumbnail.size[1]-image1.size[1])/2))
    thumbnail.paste(image1, offset)
    thumbnail.save(target, "JPEG", quality=80, optimize=True, progressive=True)
