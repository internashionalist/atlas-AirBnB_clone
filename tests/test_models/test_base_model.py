#!/usr/bin/python3

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import datetime


class BaseModelTests(unittest.TestCase):
    """
    Unittests for the BaseModel class
    """
    def setUp(self):
        """
        Setup for the unittests
        """
        self.model = BaseModel()
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up for the unittests
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save(self):
        """
        Test the save method
        """
        last_updated = self.model.updated_at
        self.model.save()
        new_updated = self.model.updated_at
        self.assertTrue(os.path.exists("file.json"))
        self.assertNotEqual(last_updated, new_updated)

    def test_to_dict(self):
        """
        Test the to_dict method
        """
        test_model = BaseModel()
        test_model_dict = BaseModel().to_dict()
        self.assertIn('id', test_model_dict)
        self.assertIn('created_at', test_model_dict)
        self.assertIn('updated_at', test_model_dict)
        self.assertIn('__class__', test_model_dict)

    def test_str(self):
        """
        Test the __str__ method
        """
        test_model = BaseModel()
        test_model.id = '1'  # mock id for testing
        test_model.created_at = datetime.datetime(2024, 9, 28, 12, 0, 0)  # mock datetime
        test_model.updated_at = datetime.datetime(2024, 9, 28, 12, 0, 0)  # mock datetime
        actual_result = str(test_model)
        expected_result = "[BaseModel] (1) {'id': '1', 'created_at': datetime.datetime(2024, 9, 28, 12, 0), 'updated_at': datetime.datetime(2024, 9, 28, 12, 0)}"
        self.assertEqual(actual_result, expected_result)
        del(test_model)

if __name__ == '__main__':
    unittest.main()
