import os
import re

from albumCover import add_album_cover
from converter import convert_temp_mp4_to_mp3
from dataRequests import download_image
from fileManager import sha1_checksum, delete_file, copy_file
from models.querys import create_track
from youtube import get_youtube_url_by_name, download_youtube_video

from constants import TEMP_PATH


class Track:
    def __init__(self, json_track, genre):
        self.artist = json_track["artist"]
        self.title = json_track["title"]
        self.image_url = json_track["imageURL"]
        self.genre = genre

        self.file_name = ''
        # paths
        self.file_path = ''
        self.temp_mp4_path = ''
        self.temp_image_path = ''
        self.temp_mp3_path = ''

        self.audio_url = ''
        self.check_sum = ''

        self.__init_file_name()
        self.__init_all_paths()

    def download(self):
        # Temp Files
        self.__search_youtube_url()
        self.__download_audio()
        self.__convert_to_mp3()
        self.__download_image()
        self.__add_album_cover()
        self.__calculate_check_sum()
        # Move Track to folder
        self.__copy_to_genre_dir()
        self.__delete_temp_files()
        # Save Track Info
        self.__db_save()

    def __search_youtube_url(self):
        self.audio_url = get_youtube_url_by_name(self.file_name)

    def __download_audio(self):
        self.temp_mp4_path = download_youtube_video(self.audio_url, self.file_name)

    def __convert_to_mp3(self):
        convert_temp_mp4_to_mp3(self.temp_mp4_path, self.temp_mp3_path)

    def __download_image(self):
        temp_image_path = os.path.join(TEMP_PATH, f"{self.file_name}.jpg")
        download_image(self.image_url, temp_image_path)
        self.temp_image_path = temp_image_path

    def __add_album_cover(self):
        add_album_cover(self.temp_mp4_path, self.temp_image_path)

    def __calculate_check_sum(self):
        self.check_sum = sha1_checksum(self.temp_mp3_path)

    def __init_file_name(self):
        name = f"{self.title} - {self.artist}"
        cleaned_name = re.sub(r'[^&a-zA-Z0-9\-(), ]+', ' ', name)
        words = cleaned_name.split()
        cleaned_name = " ".join(words)
        self.file_name = cleaned_name

    def __init_all_paths(self):
        self.file_path = os.path.join(self.genre.file_path, f"{self.file_name}.mp3")
        self.temp_mp4_path = os.path.join(TEMP_PATH, f"{self.file_name}.mp4")
        self.temp_image_path = os.path.join(TEMP_PATH, f"{self.file_name}.jpg")
        self.temp_mp3_path = os.path.join(TEMP_PATH, f"{self.file_name}.mp3")

    def __delete_temp_files(self):
        delete_file(self.temp_mp4_path)
        delete_file(self.temp_image_path)
        delete_file(self.temp_mp3_path)

    def __copy_to_genre_dir(self):
        copy_file(self.temp_mp3_path, self.genre.path)

    def __db_save(self):
        create_track(title=self.title, artist=self.artist, genre=self.genre.id, file_name=self.file_name,
                     file_path=self.file_path, image_url=self.image_url, audio_url=self.audio_url,
                     check_sum=self.check_sum)
