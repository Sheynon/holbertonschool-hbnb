from flask_restx import Namespace, Resource, fields
from app.services.facade import facade

api = Namespace('places', description='Place operations')

amenity_model = api.model('PlaceAmenity', {
    'id': fields.String,
    'name': fields.String
})

user_model = api.model('PlaceUser', {
    'id': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'email': fields.String
})

place_model = api.model('Place', {
    'title': fields.String(required=True),
    'description': fields.String,
    'price': fields.Float(required=True),
    'latitude': fields.Float(required=True),
    'longitude': fields.Float(required=True),
    'owner_id': fields.String(required=True),
    'amenities': fields.List(fields.String, required=True)
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    def post(self):
        try:
            data = api.payload
            place = facade.create_place(data)
            return place.to_dict(), 201
        except Exception as e:
            return {"error": str(e)}, 400

    def get(self):
        places = facade.get_all_places()
        return [p.to_dict(summary=True) for p in places], 200

@api.route('/<string:place_id>')
class PlaceResource(Resource):
    def get(self, place_id):
        try:
            place = facade.get_place(place_id)
            data = place.to_dict()
            data['owner'] = place.owner.to_dict()
            data['amenities'] = [a.to_dict() for a in place.amenities]
            return data, 200
        except Exception as e:
            return {"error": str(e)}, 404

    @api.expect(place_model)
    def put(self, place_id):
        try:
            data = api.payload
            place = facade.update_place(place_id, data)
            return {"message": "Place updated successfully"}, 200
        except ValueError as e:
            return {"error": str(e)}, 404
        except Exception as e:
            return {"error": str(e)}, 400
