import json
import os


def create_directory(directory_path):
    try:
        # Use the os.makedirs() function to create the directory
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_path}' already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")


def walk_and_process_directory(directory):
    directory_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                directory_list.append(file_path)
    return directory_list


def process_json_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            return data
    except Exception as e:
        print(f"Error processing JSON file {file_path}: {e}")

