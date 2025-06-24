from .places import api as places_ns

api = Api(app, version='1.0', title='HBnB API', description='HBnB REST API')
api.add_namespace(places_ns, path='/api/v1/places')
