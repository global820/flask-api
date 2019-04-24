from flask import Flask
from flask_restful import Api

from resources.listing import resource

app = Flask(__name__)
api = Api(app)

api.add_resource(resource.ListingResource, '/listing/<int:id>', endpoint='listing')

if __name__ == "__main__":
    app.run(debug=True)