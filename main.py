from constants import TOPS_PATH
from fileManager import get_files_from_dir
from genre import Genre


def download_all_top_100(files_paths):
    for file_path in files_paths:
        g = Genre(file_path)
        g.download_track_list()


if __name__ == "__main__":
    genres = get_files_from_dir(TOPS_PATH, ".json")
    download_all_top_100(genres)
