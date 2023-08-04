from concurrent.futures import ThreadPoolExecutor

from constants import TOPS_PATH, MAX_WORKERS
from fileManager import get_files_from_dir
from genre import Genre
from models.database import db  # , Genre as GenreDB, Track as TrackDB
from threads import thread_pool


def download_all_top_100(files_paths):
    for file_path in files_paths:
        g = Genre(file_path)
        thread_pool.submit(g.download_track_list)


if __name__ == "__main__":
    db.connect()
    thread_pool = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    # db.create_tables([GenreDB, TrackDB])
    genres = get_files_from_dir(TOPS_PATH, ".json")
    download_all_top_100(genres)

    thread_pool.shutdown()
