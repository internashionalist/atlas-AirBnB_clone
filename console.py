#!/usr/bin/python3
"""
Console module for AirBnB clone
"""
import cmd
import json
import models
import models.engine
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """
    Custom class for HBNB console
    """

    prompt = "(hbnb) "
    storage = None

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def __init__(self):
        """
        Initializes HBNBCommand class
        """
        super().__init__()
        self.storage = models.engine.file_storage.FileStorage()

    def do_quit(self, line):
        """
        Exits the Program
        """
        return True

    def do_EOF(self, line):
        """
        Exits the Program
        """
        return True

    def emptyline(self):
        """
        Handle's empty input + \n
        """

    def help_quit(self):
        print("Exits the program.")

    def help_EOF(self):
        print("Exits the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

