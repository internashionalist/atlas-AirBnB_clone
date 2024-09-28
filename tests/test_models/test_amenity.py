#!/usr/bin/python3
"""
Unittest for Amenity class
"""

import unittest
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
        self.amenity = Amenity()
        amenity_dict = self.amenity.to_dict()

    def tearDown(self):
        """
        TearDown for Amenity class
        """
        del self.amenity

    def test_init(self):
        """
        Test for init method
        """
        self.assertTrue(isinstance(self.amenity, BaseModel))

    def test_amenity_name(self):
        """
        Test for name input
        """
        amenity = Amenity()
        amenity.name = "Fireplace"
        self.assertEqual(amenity.name, "Fireplace")

    def test_amenity_id(self):
        """
        Test for amenity_id input
        """
        amenity = Amenity()
        amenity.amenity_id = "123"
        self.assertEqual(amenity.amenity_id, "123")

if __name__ == '__main__':
    unittest.main()