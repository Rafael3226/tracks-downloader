import os

from constants import DOWNLOADS_PATH
from fileManager import process_json_file, get_file_name, create_directory
from track import Track


class Genre:
    def __init__(self, file_path):
        self.file_path = file_path
        self.name = ''
        self.path = ''
        self.track_list = []
        self.__load_file()
        self.__set_name()
        self.__set_path()

    def __load_file(self):
        self.track_list = process_json_file(self.file_path)

    def __set_name(self):
        self.name = get_file_name(self.file_path)

    def __set_path(self):
        path = os.path.join(DOWNLOADS_PATH, self.name)
        self.path = path
        create_directory(path)

    def download_track_list(self):
        for track in self.track_list:
            t = Track(track, self)
            t.download()
