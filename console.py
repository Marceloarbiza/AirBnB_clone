#!/usr/bin/python3
"""Create a console whith cmd"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Comands to cmd"""
    prompt = '(hbnb) '

    # ----- basic hbnb commands -----
    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return(1)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return(1)


if __name__ == '__main__':
        HBNBCommand().cmdloop()
