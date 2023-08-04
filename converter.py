from moviepy.editor import *

from logger import log


def convert_temp_mp4_to_mp3(input_file, output_file):
    try:
        log.info(f"Converting '{input_file}' to MP3 format.")
        mp4 = AudioFileClip(input_file)
        log.info(f"Writing the audio to '{output_file}'.")
        mp4.write_audiofile(output_file)
        log.info("Conversion completed successfully.")
    except FileNotFoundError:
        log.error(f"File '{input_file}' not found.")
    except Exception as e:
        log.error(f"An error occurred while converting the file: {str(e)}")
