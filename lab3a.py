# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date:
# Purpose: Generate and sort 20 random values.
# Usage: ./lab3a.py

import random

values = []
for i in range(20):
    value = random.randint(0, 99)
    values.append(value)

print("Sequence:", values)

values.sort()
print("Sorted sequence:", values)


