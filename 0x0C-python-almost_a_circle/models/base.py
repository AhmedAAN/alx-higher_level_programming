#!/usr/bin/python3
"""Defines a base class."""
import json
from pathlib import Path


class Base:
    """This will be the “base” of all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Intialize a new base.

        Args:
            id (int): The id of the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumbs(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances who inherits of Base."""
        filename = cls.__name__ + '.json'
        with open(filename, "w") as file:
            if list_objs is None:
                file.write('[]')
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string.

        Args:
            json_string (str): string representing a list of dictionaries."""
        if json_string in None or json_string == '[]':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args:
            **dictionary (dict)): Double pointer to a dictionary."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_obj = cls(1, 1)
            else:
                new_obj = cls(1)
        new_obj.update(**dictionary)
        return (ne_obj)

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        path = "./" + filename
        if not path.is_file():
            return []
        with open(filename, "r") as file:
            list_objs = Base.from_json_string(file.read())
            return [cls.create(**obj) for obj in list_objs]
