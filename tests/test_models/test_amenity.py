#!/usr/bin/python3
"""
Unittest for Amenity class
"""

import unittest
import os
import json
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test for Amenity class
    """
    def setUp(self):
        """
        SetUp for Amenity class
        """
        Fireplace = Amenity()

    def tearDown(self):
        """
        TearDown for Amenity class
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """
        Test for init method
        """
        Fireplace = Amenity()
        self.assertIsEqual(type(Fireplace), Amenity)
        self.assertEqual(Fireplace.name, "")


if __name__ == '__main__':
    unittest.main()