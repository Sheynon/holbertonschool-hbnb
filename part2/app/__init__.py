from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as user_ns
from app.api.v1.amenities import api as amenities_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')

    # Placeholder pour les namespaces futurs
    api.add_namespace(user_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    return app
