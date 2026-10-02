# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 10/02/2026
# Purpose: Practice adding and removing elements in list.
# Usage: ./lab3d.py

# Follow the specific instructions given in the README.md file

mylist = [1, 2, 3, 4, 5, 6]

mylist.append(7) # Add 7 to the end of the list using the append() method
mylist.insert(0, 0) # Add 0 at the beginning of the list using the insert() method
mylist.pop(2) # Remove the element at index 2 using the pop() method
print("Modified list:", mylist)

for i in range(len(mylist)):
    if mylist[i] == 6: # Check if the element 6 is present in the list
        print(f"The element 6 is present at the index {i}.") 