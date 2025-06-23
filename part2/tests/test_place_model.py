import unittest
from models.place import Place

class TestPlaceModel(unittest.TestCase):
    def setUp(self):
        self.place = Place(
            name="Maison de vacances",
            description="Une belle maison au bord de la mer",
            longitude=45.0,
            latitude=12.5,
            price=100,
            owner="user123"
        )

    def test_attributes_initialization(self):
        self.assertEqual(self.place.name, "Maison de vacances")
        self.assertEqual(self.place.description, "Une belle maison au bord de la mer")
        self.assertEqual(self.place.longitude, 45.0)
        self.assertEqual(self.place.latitude, 12.5)
        self.assertEqual(self.place.price, 100)
        self.assertEqual(self.place.owner, "user123")
        self.assertIsInstance(self.place.reviews, list)
        self.assertIsInstance(self.place.amenities, list)

    def test_name_setter_valid(self):
        self.place.name = "Appartement"
        self.assertEqual(self.place.name, "Appartement")

    def test_name_setter_invalid(self):
        with self.assertRaises(ValueError):
            self.place.name = ""

        with self.assertRaises(ValueError):
            self.place.name = 123

    def test_description_setter_valid(self):
        self.place.description = "Description valide"
        self.assertEqual(self.place.description, "Description valide")

    def test_description_setter_invalid(self):
        with self.assertRaises(ValueError):
            self.place.description = ""

        with self.assertRaises(ValueError):
            self.place.description = 456

    def test_longitude_setter_valid(self):
        self.place.longitude = -75.5
        self.assertEqual(self.place.longitude, -75.5)

    def test_longitude_setter_invalid_type(self):
        with self.assertRaises(TypeError):
            self.place.longitude = "not a number"

    def test_longitude_setter_invalid_range(self):
        with self.assertRaises(ValueError):
            self.place.longitude = 200

        with self.assertRaises(ValueError):
            self.place.longitude = -200

    def test_latitude_setter_valid(self):
        self.place.latitude = 60.0
        self.assertEqual(self.place.latitude, 60.0)

    def test_latitude_setter_invalid_type(self):
        with self.assertRaises(TypeError):
            self.place.latitude = None

    def test_latitude_setter_invalid_range(self):
        with self.assertRaises(ValueError):
            self.place.latitude = 100

        with self.assertRaises(ValueError):
            self.place.latitude = -100

    def test_price_setter_valid(self):
        self.place.price = 150
        self.assertEqual(self.place.price, 150)

    def test_price_setter_invalid_type(self):
        with self.assertRaises(TypeError):
            self.place.price = "free"

    def test_price_setter_invalid_value(self):
        with self.assertRaises(ValueError):
            self.place.price = 0

        with self.assertRaises(ValueError):
            self.place.price = -5

    def test_owner_setter_valid(self):
        self.place.owner = "new_owner"
        self.assertEqual(self.place.owner, "new_owner")

    def test_owner_setter_invalid(self):
        with self.assertRaises(ValueError):
            self.place.owner = ""

        with self.assertRaises(ValueError):
            self.place.owner = 12345


if __name__ == "__main__":
    unittest.main()