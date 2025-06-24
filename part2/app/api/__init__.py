from flask_restx import Api
from flask import Flask

app = Flask(__name__)
api = Api(app, version='1.0', title='HBnB API', description='HBnB REST API')

from app.api.places import api as places_ns
from app.api.users import api as user_ns
from app.api.reviews import api as review_api

api.add_namespace(places_ns, path='/api/v1/places')
api.add_namespace(review_api)
api.add_namespace(user_ns)
