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

    Attributes:
        id (str):               unique id for each instance (assigned by uuid)
        created_at (datetime):  instance creation datetime
        updated_at (datetime):  instance update datetime

    Methods:
        __str__:    returns string representation of instance
        save:       updates updated_at with current datetime
        to_dict:    returns dictionary of key-value pairs
    """
