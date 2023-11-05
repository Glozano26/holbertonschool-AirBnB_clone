#!/usr/bin/python3
"""Module contain FileStorage class"""

import json
import os
from models.base_model import BaseModel
import models 

class FileStorage:
    """Serializes the instances to a JSON file and deserializes
    the JSON file into instances:"""
    __file_path = "file.json"
    __objects = {}
    
    @classmethod    
    def all(self):
        """returns the dictionary"""
        return FileStorage.__objects
    
    @classmethod
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj
    
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        new_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(new_dict, file, default=str) 

    def reload(self):
        """deserializes the JSON file"""
        try:
            with open(self.__file_path, "r") as f:
                temp_dict = json.load(f)
                for key, value in temp_dict.items():
                    class_name = value["__class__"]
                    obj_class = getattr(models, class_name)
                    instance = obj_class(**value)
                    key = "{}.{}".format(class_name, instance.id)
                    FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass