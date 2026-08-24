# ============================================================
# PROJECT PHOENIX
# LESSON 26 — NUMPY FUNDAMENTALS
# PHASE 2 — DATA SCIENCE FUNDAMENTALS
# ============================================================

# LESSON OBJECTIVES
#
# By the end of this lesson, you should understand:
#
# 1. What NumPy is
# 2. Why NumPy is useful for data science
# 3. What a NumPy array is
# 4. How to create a NumPy array
# 5. The difference between a Python list and a NumPy array
# 6. How to use basic indexing with NumPy arrays
# 7. How to perform basic numerical operations
# 8. How NumPy can be used with healthcare data


# ============================================================
# PART 1 — THE BEGINNING OF DATA SCIENCE
# ============================================================

# Lessons 1–25 focused on Python programming.
#
# Lesson 26 marks an important transition in Project Phoenix.
#
# We are now beginning:
#
# PHASE 2 — DATA SCIENCE FUNDAMENTALS
#
# We will start using Python to work with numerical data.
#
# Our first major data science library is NumPy.


# ============================================================
# PART 2 — WHAT IS NUMPY?
# ============================================================

# NumPy stands for Numerical Python.
#
# It is a Python library designed for numerical and scientific
# computing.
#
# Data science often involves working with large amounts of
# numerical data.
#
# In healthcare, this could include:
#
# - Patient ages
# - Temperatures
# - Heart rates
# - Weights
# - Laboratory measurements
#
# NumPy provides tools that make numerical calculations
# easier and more efficient.


# ============================================================
# PART 3 — INSTALLING NUMPY
# ============================================================

# Before using NumPy, it must be installed in our Python
# environment.
#
# We installed NumPy from the VS Code PowerShell terminal
# using:
#
# py -m pip install numpy
#
# Once NumPy was installed successfully, we could import it
# into our Python program.


# ============================================================
# PART 4 — IMPORTING NUMPY
# ============================================================

import numpy as np

# "np" is the conventional abbreviation for NumPy.
#
# This means that instead of writing:
#
# numpy.array(...)
#
# we can write:
#
# np.array(...)


# ============================================================
# PART 5 — OUR FIRST NUMPY ARRAY
# ============================================================

# A NumPy array is designed for working with numerical data.
#
# We create an array using np.array().

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)

# Output:
#
# [10 20 30 40 50]
#
# Notice that the NumPy array is displayed without commas.
#
# A Python list would normally be displayed as:
#
# [10, 20, 30, 40, 50]
#
# However, the missing commas are not the important difference.
#
# The important difference is that NumPy arrays are designed
# for numerical operations.


# ============================================================
# PART 6 — PYTHON LISTS VS NUMPY ARRAYS
# ============================================================

# We already learned Python lists in earlier Project Phoenix
# lessons.
#
# A Python list:

python_list = [10, 20, 30, 40, 50]

# A NumPy array:

numpy_array = np.array([10, 20, 30, 40, 50])

# Both can store multiple values.
#
# However, NumPy arrays are specifically designed for
# numerical calculations.
#
# This becomes especially useful when we want to perform
# calculations across an entire dataset.


# ============================================================
# PART 7 — ARRAY + ARRAY
# ============================================================

numbers = np.array([10, 20, 30, 40, 50])

print(numbers + numbers)

# Output:
#
# [ 20  40  60  80 100]
#
# NumPy performs the operation element by element:
#
# 10 + 10 = 20
# 20 + 20 = 40
# 30 + 30 = 60
# 40 + 40 = 80
# 50 + 50 = 100
#
# We did not need to write a loop.


# ============================================================
# PART 8 — ARRAY + A NUMBER
# ============================================================

# NumPy can also apply one number to every element
# in an array.

ages = np.array([25, 34, 41, 52, 67])

print(ages + 1)

# Output:
#
# [26 35 42 53 68]
#
# NumPy applied +1 to every value.


# ============================================================
# PART 9 — HEALTHCARE EXAMPLE: PATIENT TEMPERATURES
# ============================================================

# We created an array containing the temperatures of
# five patients.

temperatures = np.array([36.5, 37.2, 38.1, 39.0, 37.8])

print(temperatures + 0.5)

# Output:
#
# [37.  37.7 38.6 39.5 38.3]
#
# NumPy added 0.5 to every temperature.


# ============================================================
# PART 10 — BASIC INDEXING
# ============================================================

# NumPy arrays use the same basic indexing system that
# we already learned with Python lists.
#
# Example:

temperatures = np.array([36.5, 37.2, 38.1, 39.0, 37.8])

# Index:
#
# 0      1      2      3      4
#
# 36.5   37.2   38.1   39.0   37.8
#
# Therefore:

print(temperatures[3])

# Output:
#
# 39.0
#
# Remember:
#
# Indexing starts at 0.


# ============================================================
# PART 11 — BASIC NUMERICAL OPERATIONS
# ============================================================

# NumPy arrays support the basic mathematical operators
# we already know from Python.


# ADDITION

heart_rates = np.array([70, 80, 90, 100])

print(heart_rates + 5)

# Output:
#
# [ 75  85  95 105]


# SUBTRACTION

print(heart_rates - 10)

# Output:
#
# [60 70 80 90]


# MULTIPLICATION

print(heart_rates * 2)

# Output:
#
# [140 160 180 200]


# DIVISION

print(heart_rates / 2)

# Output:
#
# [35. 40. 45. 50.]
#
# Notice that division produces decimal values.


# ============================================================
# PART 12 — OPERATIONS BETWEEN TWO ARRAYS
# ============================================================

# NumPy can also perform operations between two arrays.

morning = np.array([70, 80, 90, 100])
evening = np.array([75, 85, 95, 105])

print(evening - morning)

# Output:
#
# [5 5 5 5]
#
# NumPy subtracts corresponding elements:
#
# 75  - 70  = 5
# 85  - 80  = 5
# 95  - 90  = 5
# 105 - 100 = 5


# ============================================================
# PART 13 — HEALTHCARE EXAMPLE: HEART RATES
# ============================================================

# We created an array containing five patient heart rates.

heart_rates = np.array([72, 88, 95, 110, 76])

print(heart_rates + 10)

# Output:
#
# [ 82  98 105 120  86]
#
# NumPy applied the operation to every heart rate.


# ============================================================
# PART 14 — HEALTHCARE EXAMPLE: PATIENT WEIGHTS
# ============================================================

# We created an array containing five patient weights.

weights = np.array([55, 68, 72, 81, 90])

print(weights - 5)

# Output:
#
# [50 63 67 76 85]
#
# NumPy subtracted 5 from every weight.


# ============================================================
# PART 15 — VECTORIZED OPERATIONS
# ============================================================

# When NumPy performs an operation across an entire array
# without us explicitly writing a loop, this is called a
# vectorized operation.
#
# For example:

weights = np.array([55, 68, 72, 81, 90])

print(weights - 5)

# Instead of processing each value individually, NumPy applies
# the operation across the entire array.
#
# This is one of the important differences between ordinary
# Python programming and numerical computing with NumPy.
#
# We can begin thinking:
#
# "What operation do I want to perform on the dataset?"
#
# rather than:
#
# "How do I process every value one by one?"


# ============================================================
# PART 16 — MINI HEALTHCARE EXERCISE
# ============================================================

# We created a small healthcare-oriented exercise using
# patient heart rates.
#
# Our task was to add 10 to every heart rate.

heart_rates = np.array([72, 88, 95, 110, 76])

print(heart_rates + 10)

# Output:
#
# [ 82  98 105 120  86]
#
# This demonstrates how NumPy can apply one operation
# across an entire collection of numerical data.


# ============================================================
# PART 17 — PRACTICE
# ============================================================

# PRACTICE 1
#
# Create a NumPy array containing:
#
# 10, 20, 30, 40, 50
#
# Print the array.


# PRACTICE 2
#
# Create:
#
# ages = np.array([20, 30, 40, 50])
#
# Add 5 to every age and print the result.


# PRACTICE 3
#
# Create:
#
# temperatures = np.array([36.4, 37.1, 38.2, 39.1])
#
# Add 0.2 to every temperature.


# PRACTICE 4
#
# Using:
#
# heart_rates = np.array([72, 88, 95, 110, 76])
#
# Print the value at index 3.


# PRACTICE 5
#
# Using:
#
# weights = np.array([60, 70, 80, 90])
#
# Subtract 5 from every value.


# ============================================================
# PART 18 — KEY TAKEAWAYS
# ============================================================

# 1. NumPy stands for Numerical Python.
#
# 2. NumPy is a Python library used for numerical
#    and scientific computing.
#
# 3. NumPy arrays are designed for numerical data.
#
# 4. We create arrays using np.array().
#
# 5. NumPy arrays use zero-based indexing.
#
# 6. We can perform mathematical operations across
#    an entire array.
#
# 7. We can perform operations between compatible arrays.
#
# 8. NumPy allows vectorized operations, meaning that
#    we can apply an operation across an entire dataset
#    without explicitly writing a loop.
#
# 9. NumPy is an important foundation for data science.


# ============================================================
# PROJECT PHOENIX — PHASE 2
# ============================================================

# Lessons 1–25:
#
# PYTHON PROGRAMMING FUNDAMENTALS
#
# Lesson 26:
#
# DATA SCIENCE FUNDAMENTALS BEGIN
#
# Our transition is:
#
# Python Programming
#        ↓
# NumPy
#        ↓
# Data Science
#        ↓
# Healthcare Data
#        ↓
# Healthcare AI
#
# Lesson 26 is the beginning of this transition.
#
# We are now learning to use Python not only to write
# programs, but also to work with numerical data.


# ============================================================
# LESSON 26 COMPLETE
# ============================================================

# Core concept:
#
# NumPy allows us to work with numerical datasets and
# perform mathematical operations across entire arrays.