import unittest
import uuid
from models.review import Review
from models.user import User
from models.place import Place

class TestReviewModel(unittest.TestCase):
    def setUp(self):
        # Crée un email unique pour éviter les doublons
        unique_email = f"{uuid.uuid4()}@example.com"
        self.user = User("John", "Doe", "pass123", unique_email)
        self.place = Place("Nice Place", "Great view", 10.0, 20.0, 100.0, self.user.id)

    def test_valid_review(self):
        review = Review("Very nice", 5, self.place, self.user)
        self.assertEqual(review.text, "Very nice")
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.place, self.place)
        self.assertEqual(review.user, self.user)

    def test_invalid_text_type(self):
        with self.assertRaises(ValueError):
            Review("", 4, self.place, self.user)
        with self.assertRaises(ValueError):
            Review(1234, 4, self.place, self.user)

    def test_invalid_rating_value(self):
        with self.assertRaises(ValueError):
            Review("Bad rating", 6, self.place, self.user)
        with self.assertRaises(ValueError):
            Review("Bad rating", 0, self.place, self.user)

    def test_invalid_rating_type(self):
        with self.assertRaises(TypeError):
            Review("Invalid rating", "five", self.place, self.user)

    def test_missing_place(self):
        with self.assertRaises(ValueError):
            Review("Missing place", 3, None, self.user)

    def test_missing_user(self):
        with self.assertRaises(ValueError):
            Review("Missing user", 3, self.place, None)

if __name__ == '__main__':
    unittest.main()