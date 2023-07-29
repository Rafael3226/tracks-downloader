import os
from fileManager import create_directory

APP_PATH = os.path.join("D:", "Music", "Scraped", genre)
DOWNLOADS_PATH = ""
TOPS_PATH = ""

# genre = os.path.splitext(os.path.basename(file_path))[0]
# path = os.path.join("D:", "Music", "Scraped", genre)
# create_directory(path)
#
# for track in data:
#     title = track["title"]+" - "+track["artist"]
#     video_url = search_youtube_video_url(title)
#     audioPath = os.path.join(path, title)
#     download_youtube_video(video_url, audioPath)
#     add_image_to_audio(audioPath, track["imageURL"])


# Example usage
if __name__ == "__main__":
