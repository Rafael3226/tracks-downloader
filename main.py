from constants import TOPS_PATH
from fileManager import walk_and_process_directory
from genre import Genre


def download_all_top_100(files_paths):
    for file_path in files_paths:
        g = Genre(file_path)
        g.download_track_list()


if __name__ == "__main__":
    genres = walk_and_process_directory(TOPS_PATH)
    download_all_top_100(genres)
