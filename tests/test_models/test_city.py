#!/usr/bin/python3
"""
Unittest for City class
"""

import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test for City class
    """
    def setUp(self):
        """
        SetUp for City class
        """
        self.city = City()

    def tearDown(self):
        """
        TearDown for City class
        """
        if os.path.exists("file.json"):
            os.remove

    def test_init(self):
        """
        Test for init method
        """
        Tulsa = City()
        self.assertEqual(type(Tulsa), City)
        self.assertEqual(Tulsa.state_id, "")


if __name__ == '__main__':
    unittest.main()