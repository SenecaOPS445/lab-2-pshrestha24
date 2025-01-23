#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("Error: Not enough arguments.")
    sys.exit(1)  # Exit the script with an error code

name = sys.argv[1]
age = int(sys.argv[2])  # Convert age to integer

print('Hi ' + name + ', you are ' + str(age) + ' years old.')

