#!/usr/bin/python3
"""
BaseModel class module for AirBnB clone
"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines attributes and methods for subsequent classes

    Methods:
        __str__:    returns string representation of instance
        save:       updates updated_at with current datetime
        to_dict:    returns dictionary of key-value pairs
    """
    def __init__(self, *args, **kwargs):
        """
        Method to initialize instance

        Attributes:
            id (str):               unique id for each instance
            created_at (datetime):  instance creation datetime
            updated_at (datetime):  instance update datetime
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = kwargs.get('id')
                elif key == 'created_at':
                    created_text = kwargs.get('created_at')
                    formated_text = datetime.strptime(
                        created_text, '%Y-%m-%dT%H:%M:%S.%f')
                    self.created_at = formated_text
                elif key == 'updated_at':
                    updated_text = kwargs.get('updated_at')
                    formated_text = datetime.strptime(
                        updated_text, '%Y-%m-%dT%H:%M:%S.%f')
                    self.updated_at = formated_text
                elif key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """
        Method to print string of instance
        """
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)
        # instructions say PRINT, but isn't __str__
        # supposed to return a string?

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict



# my_model = BaseModel(id=str(uuid.uuid4()),
# created_at=datetime.now().isoformat(),
# updated_at=datetime.now().isoformat())
# print(my_model)

# my_model.name = "My First Model"
# my_model.my_number = 89
# print(my_model)
# my_model.save()
# print(my_model)
# my_model_json = my_model.to_dict()
# print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
#     print("\t{}: ({}) - {}".format(key,
#       type(my_model_json[key]),
#       my_model_json[key]))
