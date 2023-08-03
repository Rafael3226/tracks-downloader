import eyed3


def add_album_cover(mp3_file, image_path):
    audiofile = eyed3.load(mp3_file)
    # Open and read the album cover image file in binary mode
    with open(image_path, "rb") as f:
        image_data = f.read()

    # Set the album cover
    audiofile.tag.images.set(3, image_data, "image/jpeg", u"Album Cover")

    # Save the changes
    audiofile.tag.save()

