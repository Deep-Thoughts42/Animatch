import os
import json

def create_character_sheet():
    open("character_sheet.json", "w").write(json.dumps(os.listdir("db")))

create_character_sheet()