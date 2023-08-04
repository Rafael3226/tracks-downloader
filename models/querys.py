from logger import log
from models.database import Genre as GenreDB, Track as TrackDB


def create_genre(name, path):
    try:
        log.info(f"Creating genre with name '{name}' and path '{path}'")
        genre = GenreDB.create(name=name, path=path)
        log.info(f"Genre created successfully: {genre}")
        return genre.id
    except Exception as e:
        log.error(f"Error occurred while creating genre: {str(e)}")
        raise e


def get_genre_by_name(genre_name):
    try:
        log.info(f"Looking up genre by name: {genre_name}")
        genre = GenreDB.get(GenreDB.name == genre_name)
        log.info(f"Genre found with ID: {genre.id}")
        return genre
    except GenreDB.DoesNotExist:
        log.info(f"Genre with name '{genre_name}' not found.")
        return None
    except Exception as e:
        log.error(f"Error occurred while looking up genre: {str(e)}")
        raise e


def get_genre_id_by_name(genre_name):
    genre = get_genre_by_name(genre_name)
    return genre.id if genre is not None else None


def create_track(title, artist, genre, file_name, file_path, image_url, audio_url, check_sum):
    try:
        log.info(f"Creating track: {title} by {artist} in genre {genre}")
        track = TrackDB.create(title=title, artist=artist, genre=genre, file_name=file_name, file_path=file_path,
                               image_url=image_url, audio_url=audio_url, check_sum=check_sum)
        log.info(f"Track created successfully: {track}")
        return track.id
    except Exception as e:
        log.error(f"Error occurred while creating track: {str(e)}")
        raise e


def get_track_by_file_name(file_name):
    try:
        log.info(f"Looking up track by file name: {file_name}")
        track = TrackDB.get(TrackDB.file_name == file_name)
        log.info(f"Track found with id: {track.id}")
        return track.id
    except TrackDB.DoesNotExist:
        log.info(f"Track with name '{file_name}' not found.")
        return None
    except Exception as e:
        log.error(f"Error occurred while looking up track: {str(e)}")
        raise e
