from bs4 import BeautifulSoup


def get_first_youtube_url(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all("a")

    for link in results:
        href = link.get("href")
        if href.startswith("/url?q=https://www.youtube.com/watch"):
            # Extract the video URL from the href
            video_url = href.split("&")[0][7:]
            return video_url
    return ''
