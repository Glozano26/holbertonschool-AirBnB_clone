#!/usr/bin/python3
"""a class model"""
import uuid
import datetime



class BaseModel():
    """a class BaseModel that defines all common attributes/methods for other classes"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        
    def save(self):
        """assign with the current datetime and will be updated"""
        self.update_at = datetime.datetime.now()
        
    def __str__(self):
        """Update a dict"""
        class_name = self.__class__.__name__
        return (f"[{class_name}] ({self.id}) {self.__dict__}")
    
    def to_dict(self):
        """returns a dictionary containing all keys/values"""

        """Gets the dictionary of the instance attributes"""
        obj_dict = self.__dict__.copy()
        
        obj_dict['__class__'] = self.__class__.__name__
        
        """converted to string object in ISO format"""
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict 

