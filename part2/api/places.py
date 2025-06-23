from flask import Blueprint, request, jsonify
from facade.place_facade import PlaceFacade
from models.place import Place

places_bp = Blueprint('places', __name__)

@places_bp.route('/places', methods=['POST'])
def create_place():
    try:
        data = request.get_json()
        place = PlaceFacade.create(data)
        return jsonify(place.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@places_bp.route('/places', methods=['GET'])
def get_all_places():
    places = PlaceFacade.retrieve()
    return jsonify([p.to_dict() for p in places]), 200

@places_bp.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    try:
        place = PlaceFacade.retrieve(place_id)
        return jsonify(place.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@places_bp.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    try:
        data = request.get_json()
        place = PlaceFacade.update(place_id, data)
        return jsonify(place.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
