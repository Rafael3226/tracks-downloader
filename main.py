import os

from albumCover import add_image_to_audio
from fileManager import create_directory, walk_and_process_directory, get_file_name, process_json_file
from youtube import search_youtube_video_url, download_youtube_video


def download_top_100():
    for file_path in genres_paths:
        track_list = process_json_file(file_path)
        genre = get_file_name(file_path)
        path = os.path.join(DOWNLOADS_PATH, genre)
        create_directory(path)

        for track in track_list:
            title = track["title"]+" - "+track["artist"]
            audio_path = os.path.join(path, title)
            video_url = search_youtube_video_url(title)
            download_youtube_video(video_url, audio_path)
            add_image_to_audio(audio_path, track["imageURL"])


# Example usage
if __name__ == "__main__":
    APP_PATH = os.path.join("D:", "TRACKS")
    DOWNLOADS_PATH = os.path.join(APP_PATH, "downloads")
    TOPS_PATH = os.path.join(APP_PATH, "tops")

    genres_paths = walk_and_process_directory(TOPS_PATH)
    download_top_100()