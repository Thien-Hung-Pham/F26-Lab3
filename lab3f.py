# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date:
# Purpose: Two Dimensional Lists
# Usage: ./lab3f.py

# Follow the specific instructions given in the README.md file

matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

element = matrix[1][2]  # Output: 6
print(element)

element = matrix[1][1]  # Output: 5
print(element)

element = matrix[0][1]  # Output: 2
print(element)

element = matrix[2][2]  # Output: 9
print(element)


for row in matrix:
    print(row)
