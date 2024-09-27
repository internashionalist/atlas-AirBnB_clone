#!/usr/bin/python3
"""
Unittest for User class
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test cases for User class
    """

    def setUp(self):
        """
        Setup test cases
        """
        self.user = User()
        self.user.email = ""
        self.user.password = ""
        self.user.first_name = ""

    def tearDown(self):
        """
        Tear down test cases
        """
        del self.user
    
    def test_init(self):
        """
        Test for init method
        """
        self.assertTrue(isinstance(self.user, BaseModel))

    def test_email(self):
        """
        Test for email input
        """
        user = User()
        user.email = "jackflash@email.com"
        self.assertEqual(user.email, "jackflash@email.com")

    def test_password(self):
        """
        Test for password input
        """
        user = User()
        user.password = "password"
        self.assertEqual(user.password, "password")

    def test_first_name(self):
        """
        Test for first_name input
        """
        user = User()
        user.first_name = "Jack"
        self.assertEqual(user.first_name, "Jack")

    def test_last_name(self):
        """
        Test for last_name input
        """
        user = User()
        user.last_name = "Flash"
        self.assertEqual(user.last_name, "Flash")

if __name__ == '__main__':
    unittest.main()