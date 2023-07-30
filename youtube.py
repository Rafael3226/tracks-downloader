from pytube import YouTube
import urllib.parse

from constants import TEMP_PATH, TEMP_MP4_NAME
from dataRequests import search_on_google
from scraping import get_first_youtube_url


def download_youtube_video(url):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        # Get the highest resolution stream (video + audio)
        video_stream = yt.streams.get_audio_only()
        # Download the video to the specified output path
        video_stream.download(TEMP_PATH, TEMP_MP4_NAME)
    except Exception as e:
        print(f"Error: {e}")


def get_youtube_url_by_name(video_name):
    search_query = urllib.parse.quote(video_name)
    response = search_on_google(search_query)
    url = get_first_youtube_url(response.text)
    return urllib.parse.unquote(url)

