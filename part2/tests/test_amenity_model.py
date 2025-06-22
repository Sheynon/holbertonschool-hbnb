import unittest
from models.amenity import Amenity

class TestAmenityModel(unittest.TestCase):
    """Tests unitaires pour la classe Amenity."""

    def test_valid_amenity_creation(self):
        """Test création valide d'une Amenity."""
        amenity = Amenity("Wi-Fi")
        self.assertEqual(amenity.name, "Wi-Fi")
        self.assertIsNotNone(amenity.id)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)

    def test_name_must_be_string(self):
        """Test que name doit être une chaîne de caractères."""
        with self.assertRaises(TypeError):
            Amenity(123)

    def test_name_cannot_be_empty(self):
        """Test que name ne peut pas être vide."""
        with self.assertRaises(ValueError):
            Amenity("")

    def test_name_max_length(self):
        """Test que name ne peut pas dépasser 50 caractères."""
        with self.assertRaises(ValueError):
            Amenity("a" * 51)

if __name__ == "__main__":
    unittest.main()