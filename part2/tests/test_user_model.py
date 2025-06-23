import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.user import User

class TestUserModel(unittest.TestCase):

    def tearDown(self):
        # Pour nettoyer les emails entre chaque test
        User._emails.clear()

    def test_create_user_valid(self):
        user = User("Alice", "Smith", "password123", "alice@example.com")
        self.assertEqual(user.first_name, "Alice")
        self.assertEqual(user.last_name, "Smith")
        self.assertEqual(user.email, "alice@example.com")
        self.assertFalse(user.is_admin)

    def test_invalid_first_name_type(self):
        with self.assertRaises(TypeError):
            User(123, "Smith", "pass", "test@example.com")

    def test_first_name_too_long(self):
        with self.assertRaises(ValueError):
            User("A" * 51, "Smith", "pass", "longname@example.com")

    def test_invalid_email_format(self):
        with self.assertRaises(ValueError):
            User("John", "Smith", "pass", "bad-email")

    def test_duplicate_email(self):
        User("Jane", "Doe", "pass", "dup@example.com")
        with self.assertRaises(ValueError):
            User("Jake", "Smith", "pass", "dup@example.com")


    def test_is_admin_not_boolean(self):
        with self.assertRaises(ValueError):
            User("Admin", "User", "pass", "admin@example.com", is_admin="yes")