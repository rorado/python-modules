import sys

def print_arguments(length: int, arguments: list):
    i = 0
    while i < length:
        print(f"Argument {i + 1}: {arguments[i]}")
        i += 1

def ft_command_quest():
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
    elif len(sys.argv) > 1:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        print_arguments(len(sys.argv) - 1, sys.argv[1:])
        print(f"Total arguments: {len(sys.argv)}")

if __name__ == "__main__":
    ft_command_quest()
