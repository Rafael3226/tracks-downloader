from pytube import YouTube
import urllib.parse

from constants import TEMP_PATH
from dataRequests import search_on_google
from logger import log
from scraping import get_first_youtube_url


def download_youtube_video(url, video_name):
    try:
        log.info(f"Downloading YouTube video: {url}")
        # Create a YouTube object
        yt = YouTube(url)
        # Get the highest resolution stream (video + audio)
        video_stream = yt.streams.get_audio_only()
        # Download the video to the specified output path
        file_path = video_stream.download(TEMP_PATH, f"{video_name}.mp4")
        log.info(f"YouTube video downloaded and saved to: {file_path}")
        return file_path
    except Exception as e:
        log.error(f"Error occurred while downloading YouTube video: {str(e)}")
        raise e


def get_youtube_url_by_name(video_name):
    try:
        search_query = urllib.parse.quote(video_name)
        log.info(f"Searching YouTube for video: {video_name}")
        response = search_on_google(search_query)
        log.info("Google search response received.")
        url = get_first_youtube_url(response.text)
        log.info(f"First YouTube URL found: {url}")
        return urllib.parse.unquote(url)
    except Exception as e:
        log.error(f"Error occurred while getting YouTube URL: {str(e)}")
        raise e

