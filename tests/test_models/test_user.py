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
        self.user = User()
        self.user.email = "jackflash@email.com"
        self.user.password = "password"
        self.user.first_name = "Jack"
        self.user.last_name = "Flash"

    def tearDown(self):
        """
        Tear down test cases
        """
        del self.user
        if os.path.exists("file.json"):
            os.remove("file.json")
    
    def test_init(self):
        """
        Test for init method
        """
        self.assertTrue(isinstance(self.user, BaseModel))
        self.assertEqual(self.user.email, "jackflash@email.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "Jack")
        self.assertEqual(self.user.last_name, "Flash")

    def test_email(self):
        """
        Test for email input
        """
        self.user.email = "jackflashTEST@email.com"
        self.assertEqual(self.user.email, "jackflashTEST@email.com")

    def test_password(self):
        """
        Test for password input
        """
        self.user.password = "password 2"
        self.assertEqual(self.user.password, "password 2")

    def test_first_name(self):
        """
        Test for first_name input
        """
        self.user.first_name = "Jackz"
        self.assertEqual(self.user.first_name, "Jackz")

    def test_last_name(self):
        """
        Test for last_name input
        """
        self.user.last_name = "Flashes"
        self.assertEqual(self.user.last_name, "Flashes")

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        user_dict = self.user.to_dict()
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')

    def test_save(self):
        """
        Test for save method
        """
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)
        self.assertGreater(self.user.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()