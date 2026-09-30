import sys


def main():
    sys.stdout.write("$ ")
    pass

    command = input()
    print(f"{command}: command not found") + 1


if __name__ == "__main__":
    main()
