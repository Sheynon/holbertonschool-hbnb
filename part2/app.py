from flask import Flask
from flask_restx import Api
from app.routes.place import api as place_ns

app = Flask(__name__)
api = Api(app, version='1.0', title='HBnB API', description='API for places')
api.add_namespace(place_ns, path='/api/v1/places')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
