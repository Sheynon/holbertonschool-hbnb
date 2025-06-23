#!/usr/bin/python3
from flask import Flask
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.teardown_appcontext
def teardown_appcontext(exception):
    """Cleanup (si tu as besoin de fermer la session DB par exemple)"""
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
