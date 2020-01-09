from flask_restful import Resource

class World(Resource):
    def get(self):
        return {'hello':'world'}, 200