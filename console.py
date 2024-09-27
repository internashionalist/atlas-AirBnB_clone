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

    def __init__(self, *args, **kwargs):
        """
        Initializes HBNBCommand class
        """
        super().__init__(*args, **kwargs)
        self.storage = models.storage

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

    def do_create(self, args):
        """
        Creates a new instance of specified class

        Usage: create <class_name>
        """
        if args == "":
            print("** class name missing **")
        elif args not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.__classes[args]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """
        Prints string representation of instance

        Usage: show <class_name> <id>
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in self.storage.all():
            print("** no instance found **")
            return
        else:
            print(self.storage.all()[key])

if __name__ == '__main__':
    HBNBCommand().cmdloop()

