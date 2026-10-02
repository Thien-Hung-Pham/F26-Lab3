# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 10/02/2026
# Purpose: Modifying a list and using the list in a loop
# Usage: ./lab3e.py

# Follow the specific instructions given in the README.md file
students = ["Ama", "Elina", "Maija", "Daniel", "Ibrahim"]

students[1] = "Maggy" # Change the second student's name to "Maggy"

for student in students:
    print(student)