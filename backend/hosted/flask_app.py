from utils import *
import random
from flask import Flask
from flask_restful import Resource, Api
import json
import os

app = Flask(__name__)
api = Api(app)

class GenerateQuestion(Resource):

    def __init__(self):
        sheet_path = os.path.join(os.getcwd(), 'mysite', 'character_sheet.json')
        with open (sheet_path, 'r') as file:
            self.data_sheet = json.load(file)
            file.close()


    def get(self):
        # sheet_path = os.path.join(os.getcwd(), 'mysite', 'character_sheet.json')
        # with open (sheet_path, 'r') as file:
        #     data_sheet = json.load(file)
        #     file.close()
        options = [random.choice(self.data_sheet) for x in range(4)]
        answer = random.choice(options)
        image_strings = create_base64_strings(answer)

        output_json = {
            "image_strings": image_strings,
            "options": options,
            "answer": answer
        }

        return output_json

api.add_resource(GenerateQuestion, "/")

if __name__ == "__main__":
    app.run("127.0.0.1", port=5000, debug=True)