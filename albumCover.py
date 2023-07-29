import requests
from pydub import AudioSegment


def download_image(image_url, output_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
            print("Image downloaded successfully.")
    else:
        print("Failed to download image.")


def add_image_to_audio(audio_path, image_url):
    output_path = audio_path
    # Download the image from the URL
    image_filename = "./temp/image.jpg"
    download_image(image_url, image_filename)

    # Load audio and image
    audio = AudioSegment.from_file(audio_path)
    image = AudioSegment.from_file(image_filename)

    # Adjust image duration to match audio duration
    image = image[:len(audio)]

    # Mix the audio with the image
    audio_with_image = audio.overlay(image)

    # Export the final audio with image
    audio_with_image.export(output_path, format="mp3")