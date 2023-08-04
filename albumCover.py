import eyed3
from logger import log


def add_album_cover(mp3_file, image_path):
    try:
        log.info(f"Loading MP3 file: {mp3_file}")
        audiofile = eyed3.load(mp3_file)

        log.info(f"Opening and reading the album cover image: {image_path}")
        with open(image_path, "rb") as f:
            image_data = f.read()

        # Set the album cover
        log.info("Setting the album cover in the MP3 file's metadata")
        audiofile.tag.images.set(3, image_data, "image/jpeg", u"Album Cover")

        # Save the changes
        log.info("Saving the changes to the MP3 file")
        audiofile.tag.save()

        log.info(f"Album cover has been added to '{mp3_file}' successfully.")
    except FileNotFoundError:
        log.error(f"File '{mp3_file}' or '{image_path}' not found.")
    except Exception as e:
        log.error(f"An error occurred while adding the album cover: {str(e)}")


