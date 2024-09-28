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
        self.amenity = Amenity()

    def tearDown(self):
        """
        TearDown for Amenity class
        """
        del self.amenity
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """
        Test for init method
        """
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_name(self):
        """
        Test for name input
        """
        self.amenity.name = "Fireplace"
        self.assertEqual(self.amenity.name, "Fireplace")

    def test_amenity_id(self):
        """
        Test for amenity_id input
        """
        self.amenity.amenity_id = "123"
        self.assertEqual(self.amenity.amenity_id, "123")

    def test_amenity_dict(self):
        """
        Test for to_dict method
        """
        amenity_dict = self.amenity.to_dict()
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertIn('__class__', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')

    def test_amenity_save(self):
        """
        Test for save method
        """
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_amenity_str(self):
        """
        Test for __str__ method
        """
        self.assertEqual(str(self.amenity), "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__))


if __name__ == '__main__':
    unittest.main()