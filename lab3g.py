# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 10/02/2026
# Purpose: Using a list in a loop and modifying the list
# Usage: ./lab3g.py

# Follow the specific instructions given in the README.md file

values = []

while len(values) < 6:
    user_input = input("Enter a number: ")
    number = int(user_input)
    values.append(number)

for i in range(len(values)):
    values[i] = values[i] * 10

values.reverse()

for value in values:
    print(value)

