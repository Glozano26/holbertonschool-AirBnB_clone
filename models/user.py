#!/usr/bin/python3
"""a class User that inherits from BaseModel"""
from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    """Public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""