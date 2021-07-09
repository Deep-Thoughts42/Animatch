from random import choice
from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class GenerateQuestion(Resource):
    def get(self):
        '''Generates a question'''
        return {
            "options": ["char_1", "char_2", "char_3", "char_4"],
            "image_paths": 
            "answer": "char_1"
        }

    def post(self):


api.add_resource(GenerateQuestion, "/")

if __name__ == "__main__":
    app.run("127.0.0.1", port=5000, debug=True)