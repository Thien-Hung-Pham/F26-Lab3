# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date:
# Purpose: Practice adding and removing elements in list.
# Usage: ./lab3d.py

# Follow the specific instructions given in the README.md file

mylist = [1, 2, 3, 4, 5, 6]

mylist.append(7)
mylist.insert(0, 0)
mylist.pop(2)
print("Modified list:", mylist)

for i in range(len(mylist)):
    if mylist[i] == 6:
        print(f"The element 6 is present at the index {i}.")