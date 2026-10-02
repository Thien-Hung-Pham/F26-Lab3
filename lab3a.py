# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 10/02/2026
# Purpose: Generate and sort 20 random values.
# Usage: ./lab3a.py

# import the random module to generate random numbers
import random

values = []
for i in range(20): 
    value = random.randint(0, 99) # Generate a random integer between 0 and 99
    values.append(value)

print("Sequence:", values)
    
values.sort()
print("Sorted sequence:", values)


