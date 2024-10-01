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
                if key == 'created_at':
                    # created_text = kwargs.get('created_at')
                    # formated_text = datetime.strptime(
                    #     created_text, '%Y-%m-%dT%H:%M:%S.%f')
                    # self.created_at = formated_text
                    if isinstance(value, str):
                        value = datetime.fromisoformat(value)
                    self.created_at = value
                elif key == 'updated_at':
                    # updated_text = kwargs.get('updated_at')
                    # formated_text = datetime.strptime(
                    #     updated_text, '%Y-%m-%dT%H:%M:%S.%f')
                    # self.updated_at = formated_text
                    if isinstance(value, str):
                        value = datetime.fromisoformat(value)
                    self.updated_at = value
                elif key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """
        Method to print string of instance
        """
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)

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
