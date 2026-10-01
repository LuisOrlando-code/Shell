import sys
import os
from itertools import count

import builtins


def main():
    commandInput()


def commandInput():
        sys.stdout.write("$ ")
        command = input()
        commandOptions(command)


def commandOptions(command):
    builtins = ["exit", "echo", "type"]
    match command.split():
        case ["exit"]:
            sys.exit()
        case ["echo", *words]:
            print(" ".join(words))
            commandInput()
        case ["type", userinput]:
            if userinput in builtins:
                print(f"{userinput} is a shell builtin")
            else:
                print(f"{userinput}: not found")
            commandInput()
        case [action, *_]:
            print(f"{command}: command not found")
            commandInput()


        case []:
            commandInput()




if __name__ == "__main__":
    main()