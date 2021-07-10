import base64
import os
import json

def create_character_sheet():
    open("character_sheet.json", "w").write(json.dumps(os.listdir("db")))

def encode_image_base64(image_path: str):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

    return encoded_string

def create_base64_strings(character_name: str):
    directory = f"db/{character_name}"

    os.chdir(directory)

    files_to_convert = [encode_image_base64(file) for file in os.listdir()]

    return files_to_convert