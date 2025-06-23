from flask import Flask
from api.places import places_bp

app = Flask(__name__)
app.register_blueprint(places_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
