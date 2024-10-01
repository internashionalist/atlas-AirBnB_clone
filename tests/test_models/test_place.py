#!/usr/bin/python3
"""
Unittest for BaseModel class
"""

import unittest
import os
from models.place import Place
from models.base_model import BaseModel



class TestPlace(unittest.TestCase):
    """
    Test for Place class
    """
    def setUp(self):
        """
        SetUp for Place class
        """
        Loft = Place()

    def tearDown(self):
        """
        TearDown for Place class
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """
        Test for init method
        """
        Loft = Place()
        self.assertIsEqual(type(Loft), Place)
        self.assertEqual(Loft.city_id, "")
        self.assertEqual(Loft.user_id, "")
        self.assertEqual(Loft.name, "")
        self.assertEqual(Loft.description, "")
        self.assertEqual(Loft.number_rooms, 0)
        self.assertEqual(Loft.number_bathrooms, 0)
        self.assertEqual(Loft.max_guest, 0)
        self.assertEqual(Loft.price_by_night, 0)
        self.assertEqual(Loft.latitude, 0.0)
        self.assertEqual(Loft.longitude, 0.0)
        self.assertEqual(Loft.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()