#!/usr/bin/env python3

"""
Defines unittests for models/user.py.
Unittest classes:
    TestUserInstantiation
    TestUserSave
    TestUserToDict
"""

import unittest
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """Test instantiation of User class."""

    def test_instance_creation(self):
        user = User()
        self.assertIsInstance(user, User)


class TestUserSave(unittest.TestCase):
    """Test saving User instances."""

    def test_save_method(self):
        user = User()
        user.save()
        self.assertIsNotNone(user.updated_at)


class TestUserToDict(unittest.TestCase):
    """Test converting User instance to dictionary."""

    def test_to_dict_method(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)


if __name__ == '__main__':
    unittest.main()
