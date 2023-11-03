#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = "(hbnb) "
    def do_quit(self, arg):
        """exit to console"""
        return True 
    def do_EOF(self, arg):
        """exit to console"""
        print()
        return True
           

if __name__ == '__main__':
    HBNBCommand().cmdloop()