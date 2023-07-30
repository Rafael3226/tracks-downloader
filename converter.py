from moviepy.editor import *


def convert_mp4_to_mp3(input_file, output_file):
    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)
