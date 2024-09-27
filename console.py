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
        Handles empty input + \n
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
        if args == "":  # if no args
            print("** class name missing **")
        elif args not in self.__classes:  # if class doesn't exist
            print("** class doesn't exist **")
        else:  # otherwise, create new instance
            new_instance = self.__classes[args]()
            new_instance.save()  # save new instance
            print(new_instance.id)  # print new instance id

    def do_show(self, args):
        """
        Prints string representation of instance

        Usage: show <class_name> <id>
        """
        args = args.split()  # split args
        if len(args) == 0:  # if no args
            print("** class name missing **")
            return
        class_name = args[0]  # get class name
        if class_name not in self.__classes:  # if class doesn't exist
            print("** class doesn't exist **")
            return
        if len(args) == 1:  # if no id
            print("** instance id missing **")
            return
        instance_id = args[1]  # get instance id
        key = "{}.{}".format(class_name, instance_id)  # create key
        if key not in self.storage.all():  # if key doesn't exist
            print("** no instance found **")
            return
        else:  # otherwise, print instance
            print(self.storage.all()[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on class name and id inputs

        Usage: destroy <class_name> <id>
        """
        args = args.split()  # split input into args
        if len(args) == 0:  # if no args
            print("** class name missing **")
            return
        class_name = args[0]  # get class name
        if class_name not in self.__classes:  # if class doesn't exist
            print("** class doesn't exist **")
            return
        if len(args) == 1:  # if no id
            print("** instance id missing **")
            return
        instance_id = args[1]  # get instance id
        key = "{}.{}".format(class_name, instance_id)  # create key
        if key not in self.storage.all():  # if key doesn't exist
            print("** no instance found **")
            return
        else:  # otherwise, delete instance
            del self.storage.all()[key]
            self.storage.save()  # save changes

if __name__ == '__main__':
    HBNBCommand().cmdloop()

