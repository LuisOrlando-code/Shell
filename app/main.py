import sys
import shutil, subprocess, os

def execute_comand(c):
    for d in os.get_exec_path():
        if os.access(fullpath := os.path.join(d, c), os.X_OK):
            return fullpath


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        try:
            command = input()
        except EOFError:
            break
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
        elif execute_command(cmd):
            subprocess.run(parts)
        else:
            print(f"{command}: not found")


if __name__ == "__main__":
    main()