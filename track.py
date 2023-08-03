import os
import re

from albumCover import add_album_cover
from converter import convert_temp_mp4_to_mp3
from dataRequests import download_image
from fileManager import sha1_checksum, delete_file
from youtube import get_youtube_url_by_name, download_youtube_video

from constants import TEMP_PATH


class Track:
    def __init__(self, json_track, genre):
        self.artist = json_track["artist"]
        self.title = json_track["title"]
        self.image_url = json_track["imageURL"]
        self.genre = genre

        self.file_name = ''
        self.file_path = ''
        self.temp_mp4_path = ''
        self.temp_image_path = ''

        self.audio_url = ''
        self.check_sum = ''

        self.__create_file_name()
        self.__create_file_path()
        self.__create_temp_mp4_path()
        self.__create_temp_image_path()

    def download(self):
        self.__search_youtube_url()
        self.__download_audio()
        self.__download_image()
        self.__convert_to_mp3()
        self.__add_album_cover()
        self.__calculate_check_sum()
        self.__delete_temp_files()

    def __calculate_check_sum(self):
        self.check_sum = sha1_checksum(self.file_path)

    def __add_album_cover(self):
        add_album_cover(self.file_path, self.temp_image_path)

    def __convert_to_mp3(self):
        convert_temp_mp4_to_mp3(self.temp_mp4_path, self.file_path)

    def __download_audio(self):
        download_youtube_video(self.audio_url)

    def __download_image(self):
        download_image(self.image_url, self.temp_image_path)

    def __search_youtube_url(self):
        self.audio_url = get_youtube_url_by_name(self.file_name)

    def __create_file_name(self):
        name = f"{self.title} - {self.artist}"
        cleaned_name = re.sub(r'[^&a-zA-Z0-9\-(), ]+', ' ', name)
        words = cleaned_name.split()
        cleaned_name = " ".join(words)
        self.file_name = cleaned_name

    def __create_file_path(self):
        self.file_path = os.path.join(self.genre.file_path, f"{self.file_name}.mp3")

    def __create_temp_mp4_path(self):
        self.temp_mp4_path = os.path.join(TEMP_PATH, f"{self.file_name}.mp4")

    def __create_temp_image_path(self):
        self.temp_image_path = os.path.join(TEMP_PATH, f"{self.file_name}.jpg")

    def __delete_temp_files(self):
        delete_file(self.temp_mp4_path)
        delete_file(self.temp_image_path)
