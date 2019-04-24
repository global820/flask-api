from flask_restful import Resource

class ListingResource(Resource):
    def get(self, id):
        return {
            'id': id
        }

    def put(self, data):
        return {
            'hello': 'world'
        }
