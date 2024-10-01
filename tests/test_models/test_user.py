#!/usr/bin/python3
"""
Unittest for User class
"""

import unittest
import os
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage



class TestUser(unittest.TestCase):
    """
    Test cases for User class
    """

    def setUp(self):
        """
        Setup test cases
        """
        test_file = "file.json"
        storage = FileStorage()

    def tearDown(self):
        """
        Tear down test cases
        """
        if os.path.exists("file.json"):
            os.remove("file.json")
    
    def test_init(self):
        """
        Test for init method
        """
        new_user = User()
        self.assertIsInstance(new_user, User)
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")

    def test_email(self):
        """
        Test for email input
        """
        new_user = User()
        new_user.email = "TEST@email.com"
        self.assertEqual(new_user.email, "TEST@email.com")

    def test_password(self):
        """
        Test for password input
        """
        new_user = User()
        new_user.password = "password 2"
        self.assertEqual(new_user.password, "password 2")

    def test_first_name(self):
        """
        Test for first_name input
        """
        new_user = User()
        new_user.first_name = "Jack"
        self.assertEqual(new_user.first_name, "Jack")

    def test_last_name(self):
        """
        Test for last_name input
        """
        new_user = User()
        new_user.last_name = "Flash"
        self.assertEqual(new_user.last_name, "Flash")

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        new_user = User()
        user_dict = new_user.to_dict()
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')

    def test_save(self):
        """
        Test for save method
        """
        new_user = User()
        old_updated_at = new_user.updated_at
        key = f"User.{new_user.id}"
        new_user.save()
        self.assertNotEqual(old_updated_at, new_user.updated_at)

if __name__ == '__main__':
    unittest.main()