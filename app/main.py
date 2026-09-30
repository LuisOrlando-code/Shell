import sys


def main():
    sys.stdout.write("$ ")
    while True:
        sys.stdout.write("$ ")

    # Wait for user input
    command = input()
    print(f"{command}: command not found") + 1
        # Wait for user input
        command = input()
        print(f"{command}: command not found")

if __name__ == "__main__":
    main()
