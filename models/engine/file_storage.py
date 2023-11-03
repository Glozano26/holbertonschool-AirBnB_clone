#!/usr/bin/python3
"""Module contain FileStorage class"""

import json

class FileStorage:
    """Serializes the instances to a JSON file and deserializes
    the JSON file into instances:"""
    def __init__(self, file_path):
        __file_path = "file.json"
        __objects = {}
    
    @classmethod    
    def all(self):
        """returns the dictionary"""
        return self.__objects
    
    @classmethod
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj
    
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, "w") as file:
            json.dump({key: v.to_dict() for key, v in self.__objects.items()}, file)
            
    def reload(self):
        """deserializes the JSON file"""
        try:
            with open(self.__file_path, "r") as f:
                temp_dict = json.load(f)
            for key, value in temp_dict.items():
                if class_name == "BaseModel":
                    from models.base_model import BaseModel
                    obj = BaseModel(**value)
                elif class_name == "User":
                    from models.user import User
                    obj = User(**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            print("File does not exist, impossible to load data")
        except Exception as ex:
            print(f"Error durante la carga: {ex}")