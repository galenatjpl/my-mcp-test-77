#!/usr/bin/env python3
import sys
import os

def read_numbers_from_args(args):
    try:
        return [float(arg) for arg in args]
    except ValueError:
        print("Error: All arguments must be numbers.")
        sys.exit(1)

def read_numbers_from_file(filename):
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' does not exist.")
        sys.exit(1)
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            for part in line.strip().split():
                try:
                    numbers.append(float(part))
                except ValueError:
                    print(f"Warning: Skipping non-numeric value '{part}' in file.")
    if not numbers:
        print("Error: No valid numbers found in file.")
        sys.exit(1)
    return numbers

def main():
    if len(sys.argv) < 2:
        print("Usage: python sort_numbers.py <num1> <num2> ... | <filename>")
        sys.exit(1)
    # If the first argument is a file, read from file
    if len(sys.argv) == 2 and os.path.isfile(sys.argv[1]):
        numbers = read_numbers_from_file(sys.argv[1])
    else:
        numbers = read_numbers_from_args(sys.argv[1:])
    numbers.sort()
    print("Sorted numbers:", ' '.join(str(n) for n in numbers))

if __name__ == "__main__":
    main()
