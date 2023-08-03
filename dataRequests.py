import requests


def search_on_google(search_query):
    search_url = f"https://www.google.com/search?q={search_query}"
    response = requests.get(search_url)
    response.raise_for_status()
    return response


def download_image(image_url, output_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
    else:
        print("Failed to download image.")


