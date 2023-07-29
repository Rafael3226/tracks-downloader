from pytube import YouTube


def download_youtube_video(url, output_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream (video + audio)
        video_stream = yt.streams.filter(only_audio=True).all()

        # Download the video to the specified output path
        video_stream.download(output_path)
    except Exception as e:
        print(f"Error: {e}")


def search_youtube_video_url(search_query):
    try:
        # Perform the search on YouTube
        search_results = YouTube(
            f'https://www.youtube.com/results?search_query={search_query}')

        # Get the URL of the first video from the search results
        video_url = f'https://www.youtube.com/watch?v={search_results.video_urls[0]}'

        return video_url
    except Exception as e:
        print(f"Error: {e}")
        return ''
