import json
import os

def generate_json():
    files = os.listdir("characters")

    data = {}

    for file in files:
        character_name = file[:-4:]

        data[character_name] = f"characters/{file}"

    data_json = json.dumps(data)

    with open("character_data.json", "w") as fp:
        fp.write(data_json)

if __name__ == "__main__":
    generate_json()