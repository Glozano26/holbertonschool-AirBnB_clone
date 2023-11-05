#!/usr/bin/python3
"""Firts Console"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
import json

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("Exit")
        return True
    
    def do_EOF(self, arg):
        """Exit the Program"""
        print("Exit")
        return True
    
    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """new instance of BaseModel, saves it (to the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.strip()
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return 
        
        new_instance = eval(class_name)()
        new_instance.save()
        
        print(new_instance.id)
    
    def do_show(self, arg):
        """ Prints the string representation of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            key = class_name + "." + args[1]
            all_objs = models.storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
    
    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            key = class_name + "." + args[1]
            all_objs = models.storage.all()
            if key in all_objs:
                del all_objs[key]
                models.storage.save()
            else:
                print("** no instance found **")
    
    def all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        obj_dict = models.storage.all()

        if not arg:
            for key in obj_dict:
                print (str(obj_dict[key]))
        elif not any(key.startswith(arg + ".") for key in obj_dict):
            print("** class doesn't exist **")
        else:
            print([str(obj_dict[key]) for key in obj_dict if key.startswith(arg + ".")])
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()