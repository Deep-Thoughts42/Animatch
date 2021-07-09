from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class GenerateQuestion(Resource):
    def get(self):
        return {"hello" : "world"}

api.add_resource(GenerateQuestion, "/")

if __name__ == "__main__":
    app.run("127.0.0.1", port=5000, debug=True)