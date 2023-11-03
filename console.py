#!/usr/bin/python3
"""Firts Console"""
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

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
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
