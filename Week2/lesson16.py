"""
===========================================
Project Phoenix - Week 2 - Lesson 16
Modules and the Python Standard Library
===========================================

Topics Covered
--------------
1. What is a module?
2. Importing modules
3. Importing specific functions
4. Module aliases
5. Creating your own modules
6. Python Standard Library
7. math module
8. random module

Author: Bess K.
"""

# ===========================================
# PART 1 - Importing a Module
# ===========================================

print("========== PART 1 ==========")

import math

print("Square root of 81:", math.sqrt(81))
print("Value of pi:", math.pi)


# ===========================================
# PART 2 - Importing a Specific Function
# ===========================================

print("\n========== PART 2 ==========")

from math import sqrt

print("Square root of 144:", sqrt(144))


# ===========================================
# PART 3 - Module Alias
# ===========================================

print("\n========== PART 3 ==========")

import math as m

print("Square root of 64:", m.sqrt(64))
print("Pi:", m.pi)


# ===========================================
# PART 4 - Useful Math Functions
# ===========================================

print("\n========== PART 4 ==========")

print("Ceiling of 7.2:", math.ceil(7.2))
print("Floor of 7.8:", math.floor(7.8))
print("3 raised to the power 3:", math.pow(3, 3))
print("Factorial of 4:", math.factorial(4))


# ===========================================
# PART 5 - Area of a Circle
# ===========================================

print("\n========== PART 5 ==========")

radius = 8
area = math.pi * radius ** 2

print(f"Area of the circle: {area:.2f}")


# ===========================================
# PART 6 - Circumference of an MRI Room
# ===========================================

print("\n========== PART 6 ==========")

radius = 12
circumference = 2 * math.pi * radius

print(f"MRI room circumference: {circumference:.2f} meters")


# ===========================================
# PART 7 - Random Module
# ===========================================

print("\n========== PART 7 ==========")

import random

hospital_departments = [
    "Emergency",
    "Pharmacy",
    "Surgery",
    "Pediatrics",
    "Radiology"
]

selected_department = random.choice(hospital_departments)

print(f"Today's audit department: {selected_department}")


# ===========================================
# PART 8 - Creating Your Own Module
# ===========================================

print("\n========== PART 8 ==========")

print("""
Example:

hospital_math.py

import math

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 1)

def calculate_bsa(weight, height):
    bsa = math.sqrt((height * weight) / 3600)
    return round(bsa, 2)


main.py

import hospital_math

bmi = hospital_math.calculate_bmi(70, 1.75)
print(f"BMI: {bmi}")

bsa = hospital_math.calculate_bsa(70, 175)
print(f"BSA: {bsa}")
""")


# ===========================================
# LESSON SUMMARY
# ===========================================

print("\n========== LESSON SUMMARY ==========")

print("""
A module is simply a Python file containing reusable code.

Ways to import modules:

1. import math
   -> math.sqrt(81)

2. from math import sqrt
   -> sqrt(81)

3. import math as m
   -> m.sqrt(81)

Useful math functions:

math.sqrt()        Square root
math.pi            Pi constant
math.ceil()        Round up
math.floor()       Round down
math.pow()         Raise to a power
math.factorial()   Factorial

Useful random function:

random.choice(list)

Professional Software Engineering Principles:

✓ Organize code into modules.
✓ Each module should have one responsibility.
✓ Reuse functions instead of copying code.
✓ Put imports at the top of the file.
✓ Use meaningful variable names.
✓ Read error messages carefully.
✓ Think about project structure, not just syntax.

Healthcare Examples:

• BMI calculator
• Body Surface Area calculator
• Random department audit
• MRI room circumference

Modules are one of the foundations of professional Python
development and will be used extensively in Data Science,
Machine Learning, and Healthcare AI.
""")