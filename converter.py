from moviepy.editor import *

from constants import TEMP_MP4_PATH


def convert_temp_mp4_to_mp3(output_file):
    mp4 = AudioFileClip(TEMP_MP4_PATH)
    mp4.write_audiofile(output_file)
