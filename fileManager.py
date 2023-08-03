import json
import os
import hashlib

from logger import logger


def sha1_checksum(file_path):
    sha1_hash = hashlib.sha1()

    with open(file_path, "rb") as f:
        # Read the file in chunks to avoid memory issues with large files
        while chunk := f.read(8192):
            sha1_hash.update(chunk)

    return sha1_hash.hexdigest()


def create_directory(directory_path):
    try:
        if not directory_exists(directory_path):
            os.makedirs(directory_path)
        return True
    except Exception as e:
        logger.error(e)
        return False


def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError as e:
        logger.warning(e)
    except Exception as e:
        logger.error(e)


def get_files_from_dir(directory, extension=''):
    directory_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                directory_list.append(file_path)
    return directory_list


def process_json_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            return data
    except Exception as e:
        logger.error(e)


def get_file_name(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]


def directory_exists(directory_path):
    return os.path.exists(directory_path) and os.path.isdir(directory_path)
