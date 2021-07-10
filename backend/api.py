import random
from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class GenerateQuestion(Resource):
    def __init__(self):
        self.data_sheet = json.load(open("character_sheet.json"))

    def get(self):
        options = [random.choice(self.data_sheet) for x in range(4)]
        answer = random.choice(options)

        output_json = {
            "options": options,
            "answer": answer
        }

        return output_json

api.add_resource(GenerateQuestion, "/")

if __name__ == "__main__":
    app.run("127.0.0.1", port=5000, debug=True)