import eyed3

from constants import TEMP_IMAGE_PATH
from dataRequests import download_image


def add_album_cover(mp3_file):
    audiofile = eyed3.load(mp3_file)
    # Open and read the album cover image file in binary mode
    with open(TEMP_IMAGE_PATH, "rb") as f:
        image_data = f.read()

    # Set the album cover
    audiofile.tag.images.set(3, image_data, "image/jpeg", u"Album Cover")

    # Save the changes
    audiofile.tag.save()

