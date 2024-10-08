#!/usr/bin/python3
"""
Console module for AirBnB clone
"""
import cmd
import json
import models
import models.engine
import re
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
        Handles empty input
        """
        pass

    def do_create(self, line):
        """
        Creates and saves a new BaseModel instance and prints the id

        Usage: create <class name>
        """
        if line.strip():
            if line in HBNBCommand.__classes:
                new_obj = HBNBCommand.__classes[line]()
                storage.new(new_obj)
                storage.save()
                print(new_obj.id)
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
            if line_splits[0] in HBNBCommand.__classes:
                if len(line_splits) > 1:
                    storage_id = '{}.{}'.format(line_splits[0], line_splits[1])
                    if storage_id in storage.all():
                        print(storage.all()[storage_id])
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_destroy(self, line):
        """
        Deletes a specific object based on input from storage

        Usage: destroy <class name> <id>
        """
        if line.strip():
            line_splits = re.findall(r'\"(.*?)\"|(\S+)', line)
            line_splits = [elem for tup in line_splits for elem in tup if elem]
            if line_splits[0] in self.__classes:
                if len(line_splits) > 1:
                    storage_id = f"{line_splits[0]}.{line_splits[1]}"
                    if storage_id in storage.all():
                        del storage.all()[storage_id]
                        storage.save()
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_all(self, line):
        """
        Prints string representation of all instances in storage
        or of all of a specific class

        Usage:  all <class name>
                <class name>.all()
        """
        line_splits = line.strip().split()
        if line_splits:
            class_name = line_splits[0]
        else:
            class_name = line
        if class_name:
            if class_name in HBNBCommand.__classes:
                list_models = []
                for key, value in storage.all().items():
                    if key.split('.')[0] == class_name:
                        list_models.append(str(value))
                print(list_models)
            else:
                print("** class doesn't exist **")
        else:
            list_models = []
            for key, value in storage.all().items():
                list_models.append(str(value))
            print(list_models)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updtting attribute and save the changes

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if line.strip():
            line_splits = re.findall(r'\"(.*?)\"|(\S+)', line)
            line_splits = [elem for tup in line_splits for elem in tup if elem]
            if line_splits[0] in HBNBCommand.__classes:
                if len(line_splits) > 1:
                    storage_id = '{}.{}'.format(line_splits[0], line_splits[1])
                    storage = models.storage.all()
                    if storage_id in storage:
                        if len(line_splits) > 2:
                            if len(line_splits) > 3:
                                setattr(storage[storage_id], line_splits[2],
                                        line_splits[3])
                                storage[storage_id].save()
                            else:
                                print('** value missing **')
                        else:
                            print('** attribute name missing **')
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def default(self, line):
        """
        Handles prefixed commands
        """
        if line.endswith('.all()'):
            class_name = line.split('.')[0]
            if class_name in HBNBCommand.__classes:
                list_models = []
                for key, value in storage.all().items():
                    if key.split('.')[0] == class_name:
                        list_models.append(str(value))
                print(list_models)
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax: {}".format(line))

    def help_quit(self):
        print("Exits the program.")

    def help_EOF(self):
        print("Exits the program")

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
