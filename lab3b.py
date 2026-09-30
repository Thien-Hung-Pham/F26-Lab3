# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date:
# Purpose: Reverse a list of values.
# Usage: ./lab3b.py

# Follow the specific instructions given in the README.md file

"""Return a new list that is the reverse of the input list."""
def reverse_list(lst):
    return lst[::-1]

list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(list)
print("Original list:", list)
print("Reversed list:", reversed_list)