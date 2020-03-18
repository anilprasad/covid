import os
import uuid

from PIL import Image
from django.conf import settings


def scramble_uploaded_filename(instance, filename):
    """
    Scramble / uglify the filename of the uploaded file, but keep the files extension (e.g., .jpg or .png)
    :param instance:
    :param filename:
    :return:
    """
    extension = filename.split(".")[-1]
    name = "{}.{}".format(uuid.uuid4(), extension)
    return name


def create_thumbnail(input_image, thumbnail_size=(256, 256)):
    """
    Create a thumbnail of an existing image
    :param input_image:
    :param thumbnail_size:
    :return:
    """
    # make sure an image has been set
    if not input_image or input_image == "":
        return

    # open image
    image = Image.open(input_image)

    # use PILs thumbnail method; use anti aliasing to make the scaled picture look good
    image.thumbnail(thumbnail_size, Image.ANTIALIAS)

    # parse the filename and scramble it
    filename = scramble_uploaded_filename(None, os.path.basename(input_image.name))
    arrdata = filename.split(".")
    # extension is in the last element, pop it
    extension = arrdata.pop()
    basename = "".join(arrdata)
    # add _thumb to the filename
    new_filename = basename + "_thumb." + extension

    # save the image in MEDIA_ROOT and return the filename
    image.save(os.path.join(settings.MEDIA_ROOT, new_filename))

    return new_filename