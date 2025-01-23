#!/usr/bin/env python3
# Author: Your Full Name
# Author ID: Your Seneca ID
# Date Created: yyyy/mm/dd

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3  # Default value if no argument is given

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
