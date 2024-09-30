#!/usr/bin/python3

import unittest
import os
from models.base_model import BaseModel
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

    def tearDown(self):
        """
        Clean up for the unittests
        """
        del self.model
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save(self):
        """
        Test the save method
        """
        test_model = BaseModel()
        test_model.save()
        self.assertNotEqual(test_model.created_at,
                            test_model.updated_at)

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

# my_model = BaseModel()
# my_model.name = "My First Model"
# my_model.my_number = 89
# print(my_model)
# my_model.save()
# print(my_model)
# my_model_json = my_model.to_dict()
# print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
#     print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
