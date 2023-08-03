from moviepy.editor import *


def convert_temp_mp4_to_mp3(input_file, output_file):
    mp4 = AudioFileClip(input_file)
    mp4.write_audiofile(output_file)
