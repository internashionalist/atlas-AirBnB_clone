import unittest
from models.base_model import BaseModel


class BaseModelTests(unittest.TestCase):
    def testSave(self):
        model = BaseModel()
        old_update = model.updated_at
        model.save()
        actual_result = model.updated_at
        self.assertNotEqual(actual_result, old_update)



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
