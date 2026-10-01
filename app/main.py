import subprocess
import sys
import os

def main():
    # TODO: Uncomment the code below to pass the first stage
    BUILTINS = ["type", "echo", "exit", "pwd"]
    while True:
        sys.stdout.write("$ ")
        line = input()
        if not line:
            continue

        tokens = line.split()
        command = tokens[0]
        args = tokens[1:]
        if command == "echo":
            print(*args)
        elif command == "exit":
            sys.exit(0)
        elif command == "pwd":
            print(os.getcwd())


        elif command == "type":
            if not args:
                continue
            target = args[0]
            if target in BUILTINS:
                print(f"{target} is a shell builtin")
            else:
                path = dir_path(target)
                if path:
                    print(f"{target} is {path}")
                else:
                    print(f"{target}: not found")
        else:
            target_prg_path = dir_path(command)
            if not target_prg_path:
                print(f"{command}: command not found")
            else:
                subprocess.run(args=tokens, executable=target_prg_path)


    
def dir_path(cmd):
    path = os.environ.get("PATH", "")
    for dir in path.split(":"):
        path_to_cmd = os.path.join(dir, cmd)
        if os.path.isfile(path_to_cmd) and os.access(path_to_cmd, os.X_OK):
            return path_to_cmd
    return None


if __name__ == "__main__":
    main()