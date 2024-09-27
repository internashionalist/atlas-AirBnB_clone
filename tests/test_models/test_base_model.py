import unittest
from models.base_model import BaseModel


class BaseModelTests(unittest.TestCase):
    def testSave(self):
        model = BaseModel()
        old_update = model.updated_at
        model.save()
        actual_result = model.updated_at
        self.assertNotEqual(actual_result, old_update)
    def testToDict(self):
        model_to_dict = BaseModel().to_dict()
        self.assertEqual(len(model_to_dict), 4)
    def testStr(self):
        model = BaseModel()
        model.id = '1'  # mock id for testing
        model.created_at = '2024'
        model.updated_at = '2024'
        actual_result = str(model)
        expected_result = "[BaseModel] (1) {'id': '1', 'created_at': '2024', 'updated_at': '2024'}"
        self.assertEqual(actual_result, expected_result)

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
