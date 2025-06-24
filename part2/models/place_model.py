from flask_restx import Namespace, Resource, fields

place_ns = Namespace('places', description='Place operations')

review_model = place_ns.model('PlaceReview', {
    'id': fields.String,
    'text': fields.String,
    'rating': fields.Integer,
    'user_id': fields.String
})

place_model = place_ns.model('Place', {
    'id': fields.String,
    'title': fields.String,
    'description': fields.String,
    'price': fields.Float,
    'latitude': fields.Float,
    'longitude': fields.Float,
    'owner_id': fields.String,
    'amenities': fields.List(fields.String),
    'reviews': fields.List(fields.Nested(review_model))
})
