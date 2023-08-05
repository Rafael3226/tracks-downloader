from concurrent.futures import ThreadPoolExecutor

from constants import TOPS_PATH, MAX_WORKERS
from fileManager import get_files_from_dir
from genre import Genre
from models.database import db  # , Genre as GenreDB, Track as TrackDB
from threads import thread_pool


def download_all_top_100(files_paths):
    for file_path in files_paths:
        g = Genre(file_path)
        g.download_track_list()


def fix_images(files_paths):
    for file_path in files_paths:
        g = Genre(file_path)
        g.fix_images_from_list()


if __name__ == "__main__":
    db.connect()
    # db.create_tables([GenreDB, TrackDB])
    genres = get_files_from_dir(TOPS_PATH, ".json")
    fix_images(genres)
    thread_pool.shutdown()
