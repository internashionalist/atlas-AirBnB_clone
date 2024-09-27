#!/usr/bin/python3
"""
BaseModel class module for AirBnB clone
"""

#import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines attributes and methods for subsequent classes

    Attributes:
        id (str):               unique id for each instance (assigned by uuid)
        created_at (datetime):  instance creation datetime
        updated_at (datetime):  instance update datetime

    Methods:
        __str__:    returns string representation of instance
        save:       updates updated_at with current datetime
        to_dict:    returns dictionary of key-value pairs
    """
    def __init__(self):
        """
        Method to initialize instance

        Attributes:
            id (str):               unique id for each instance (assigned by uuid)
            created_at (datetime):  instance creation datetime
            updated_at (datetime):  instance update datetime

        Returns:
            None
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Method to print string of instance"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)
        # instructions say PRINT, but isn't __str__ supposed to return a string?

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

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



