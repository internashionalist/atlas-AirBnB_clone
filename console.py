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
from models.engine.file_storage import FileStorage
from models import storage


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
        Handle's empty input
        """
        pass

    def help_quit(self):
        print("Exits the program.")

    def help_EOF(self):
        print("Exits the program")

    def do_create(self, line):
        """
        Creates and saves a new BaseModel instance and prints the id.
        """
        if line.strip():
            if line == 'BaseModel':
                new_model = BaseModel()
                storage.new(new_model)
                storage.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Shows a specific BaseModel object based on input

        Usage: show <class name> <id>
        """
        if line.strip():
            line_splits = line.split()
            if line_splits[0] == 'BaseModel':
                if len(line_splits) > 1:
                    storage_id = 'BaseModel.{}'.format(line_splits[1])
                    if storage_id in storage.all():
                        print(storage.all()[storage_id])
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        else:
            print('** class name is missing **')

    def do_destroy(self, line):
        """
        Deletes a specific object based on input from storage

        Usage: destroy <class name> <id>
        """
        if not line.strip():
            print('** class name missing **')
            return
        line_splits = line.split()
        if line_splits[0] not  in self.__classes:
            print("** class doesn't exist **")
            return
        if len(line_splits) < 2:
            print('** instance id missing **')
            return
        storage_id = f"{line_splits[0]}.{line_splits[1]}"
        if storage_id not in storage.all():
            print('** no instance found **')
            return
        del storage.all()[storage_id]
        storage.save()

    def do_all(self, line):
        """
        Prints string representation of all instances in storage
        or of all of a specific class

        Usage: all <class name>
        """
        if line.strip():
            if line == 'BaseModel':
                list_models = []
                for key, value in storage.all().items():
                    if key.split('.')[0] == 'BaseModel':
                        list_models.append(str(value))
                print(list_models)
            else:
                print("** class doesn't exist **")
        else:
            list_models = []
            for key, value in storage.all().items():
                list_models.append(str(value))
            print(list_models)

    def do_update(self, line):  # might re-write with regex to handle double quotes
        """
        Updates an instance based on the class name and id
        by adding or updtting attribute and save the changes

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not line.strip():
            print('** class name missing **')
            return
        line_splits = line.split()
        if line_splits[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(line_splits) < 2:
            print('** instance id missing **')
            return
        storage_id = f"{line_splits[0]}.{line_splits[1]}"
        if storage_id not in storage.all():
            print('** no instance found **')
            return
        if len(line_splits) < 3:
            print('** attribute name missing **')
            return
        if len(line_splits) < 4:
            print('** value missing **')
            return
        if len(line_splits) > 4:
            line_splits[3] = ' '.join(line_splits[3:])
        setattr(storage.all()[storage_id], line_splits[2], line_splits[3])
        storage.save()

    def help_create(self):
        print('Creates and saves a new BaseModel instance and prints the id.')

    def help_show(self):
        print('Shows a specific BaseModel object based on input.')

    def help_destroy(self):
        print('Deletes a specific BaseModel object stored in storage.')

    def help_all(self):
        print('Prints string representation of all instances in storage or \
              of all of a specific class')

    def help_update(self):
        print('Updates an instance based on the class name and id \
        by adding or updtting attribute and save the changes')


if __name__ == '__main__':
    HBNBCommand().cmdloop()

