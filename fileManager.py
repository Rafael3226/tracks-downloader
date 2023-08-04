import json
import os
import hashlib
import shutil

from logger import log


def sha1_checksum(file_path):
    try:
        log.info(f"Calculating SHA-1 checksum for file: {file_path}")
        sha1_hash = hashlib.sha1()

        with open(file_path, "rb") as f:
            # Read the file in chunks to avoid memory issues with large files
            while chunk := f.read(8192):
                sha1_hash.update(chunk)

        checksum = sha1_hash.hexdigest()
        log.info(f"SHA-1 checksum: {checksum}")
        return checksum
    except Exception as e:
        log.error(f"Error occurred while calculating checksum: {str(e)}")
        raise e


def create_directory(directory_path):
    try:
        log.info(f"Creating directory: {directory_path}")
        if not directory_exists(directory_path):
            os.makedirs(directory_path)
            log.info("Directory created successfully.")
        return True
    except Exception as e:
        log.error(f"Error occurred while creating directory: {str(e)}")
        return False


def delete_file(file_path):
    try:
        log.info(f"Deleting file: {file_path}")
        os.remove(file_path)
        log.info("File deleted successfully.")
    except FileNotFoundError as e:
        log.warning(f"File not found: {str(e)}")
    except Exception as e:
        log.error(f"Error occurred while deleting file: {str(e)}")


def get_files_from_dir(directory, extension=''):
    try:
        log.info(f"Listing files in directory: {directory}")
        directory_list = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(root, file)
                    directory_list.append(file_path)
        log.info(f"Found {len(directory_list)} files with extension '{extension}'")
        return directory_list
    except Exception as e:
        log.error(f"Error occurred while listing files: {str(e)}")
        raise e


def process_json_file(file_path):
    try:
        log.info(f"Processing JSON file: {file_path}")
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            log.info("JSON file processed successfully.")
            return data
    except Exception as e:
        log.error(f"Error occurred while processing JSON file: {str(e)}")
        raise e


def get_file_name(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]


def directory_exists(directory_path):
    return os.path.exists(directory_path) and os.path.isdir(directory_path)


def copy_file(source_file, destination_file):
    try:
        log.info(f"Copying file from '{source_file}' to '{destination_file}'")
        shutil.copy(source_file, destination_file)
        log.info("File copied successfully.")
    except Exception as e:
        log.error(f"An error occurred while copying the file: {str(e)}")
        raise e
