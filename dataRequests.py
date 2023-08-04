import requests

from logger import log


def search_on_google(search_query):
    try:
        log.info(f"Searching on Google: {search_query}")
        search_url = f"https://www.google.com/search?q={search_query}"
        response = requests.get(search_url)
        response.raise_for_status()
        log.info("Google search successful.")
        return response
    except requests.exceptions.RequestException as e:
        log.error(f"Error occurred while searching on Google: {str(e)}")
        raise e


def download_image(image_url, output_path):
    try:
        log.info(f"Downloading image from URL: {image_url}")
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            log.info(f"Image downloaded and saved to: {output_path}")
        else:
            log.warning(f"Request to image failed: {image_url}")
    except requests.exceptions.RequestException as e:
        log.error(f"Error occurred while downloading image: {str(e)}")
        raise e


