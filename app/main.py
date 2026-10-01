import sys
import shutil


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        try:
            command = input()
        except EOFError:
            break
        if command == "type":
            main()
        else:
            pass
        if command == "exit":
            break
        if command.startswith("echo "):
            print(f"{command[5:]}")
        elif command.startswith("type "):
            cmd = command[5:]
            if cmd in ["echo", "exit", "type"]:
                print(f"{cmd} is a shell builtin")
            elif path := shutil.which(cmd):
                print(f"{cmd} is {path}")
            else:
                print(f"{cmd}: not found")
        else:
            print(f"{command}: not found")


if __name__ == "__main__":
    main()