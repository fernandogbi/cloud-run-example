from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from app.resources.hello import World
api.add_resource(World,'/',methods=['GET'])