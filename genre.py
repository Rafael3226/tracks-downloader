import os
from concurrent.futures import ThreadPoolExecutor

from constants import DOWNLOADS_PATH, MAX_WORKERS
from fileManager import process_json_file, get_file_name, create_directory
from logger import log
from models.querys import get_genre_id_by_name, create_genre
from threads import thread_pool
from track import Track


class Genre:
    def __init__(self, file_path):
        self.id = ''
        self.file_path = file_path
        self.name = ''
        self.path = ''
        self.track_list = []
        self.__load_file()
        self.__set_name()
        self.__set_path()
        self.__get_id()

    def __load_file(self):
        self.track_list = process_json_file(self.file_path)

    def __set_name(self):
        self.name = get_file_name(self.file_path)

    def __set_path(self):
        path = os.path.join(DOWNLOADS_PATH, self.name)
        self.path = path
        create_directory(path)

    def download_track_list(self):
        for json_track in self.track_list:
            thread_pool.submit(self.__download_track, json_track)

    def __download_track(self, json_track):
        try:
            t = Track(json_track, self)
            t.download()
        except Exception as e:
            log.error(f"Error occurred while downloading track: {str(e)}")

    def __get_id(self):
        genre_id = get_genre_id_by_name(self.name)
        if genre_id is None:
            genre_id = create_genre(name=self.name, path=self.path)
        self.id = genre_id
