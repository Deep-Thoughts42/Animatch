import base64
import os
import json

def create_character_sheet():
    cur_dir = os.getcwd()
    required_path = os.path.join(cur_dir, 'mysite', 'character_sheet.json')
    open(required_path, "w").write(json.dumps(os.listdir("db")))

def encode_image_base64(image_path: str):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

    return encoded_string

def create_base64_strings(character_name: str):
    cur_dir = os.getcwd()
    required_path = os.path.join(cur_dir, 'mysite', 'db', character_name)


    files_to_convert = [encode_image_base64(os.path.join(cur_dir, 'mysite', 'db', character_name, file)) for file in os.listdir(required_path)]


    return files_to_convert