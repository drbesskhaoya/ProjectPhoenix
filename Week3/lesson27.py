# ============================================================
# PROJECT PHOENIX
# LESSON 27 — NumPy in Practice
# ============================================================

# ============================================================
# LESSON GOALS
# ============================================================
#
# By the end of this lesson, you will be able to:
#
# 1. Filter NumPy arrays using Boolean conditions.
# 2. Find values outside a reference range.
# 3. Calculate how far values are outside a range.
# 4. Calculate mean, minimum, maximum, standard deviation,
#    and range.
# 5. Work with 2D NumPy arrays.
# 6. Understand axis=0 and axis=1.
# 7. Select columns from a 2D array.
# 8. Filter complete rows based on a condition.
# 9. Combine multiple conditions using & and |.
# 10. Apply these techniques to healthcare data.


# ============================================================
# PART 1 — BOOLEAN FILTERING
# ============================================================
#
# NumPy allows us to test every value in an array against
# a condition.
#
# Each value produces either True or False.
#
# Example:
#
# bp = [118, 142, 135, 160, 125, 148, 110]
#
# Condition:
#
# bp >= 140
#
# NumPy checks every value individually.
#
# Result:
#
# [False, True, False, True, False, True, False]


import numpy as np

bp = np.array([118, 142, 135, 160, 125, 148, 110])

print(bp >= 140)

# Output:
# [False  True False  True False  True False]


# ============================================================
# PART 2 — FILTERING AN ARRAY
# ============================================================
#
# A Boolean condition can be used to filter the array.
#
# The pattern is:
#
# array[condition]
#
# Example:
#
# Find all BP values >= 140.


high_bp = bp[bp >= 140]

print(high_bp)

# Output:
# [142 160 148]


# ============================================================
# PART 3 — VALUES OUTSIDE A REFERENCE RANGE
# ============================================================
#
# Suppose the reference range for this example is:
#
# 90–139 mmHg
#
# We want values:
#
# below 90 OR above 139
#
# In NumPy:
#
# | means OR
#
# Each condition should be placed inside parentheses.


outside_range = (bp < 90) | (bp > 139)

print(bp[outside_range])

# Output:
# [142 160 148]


# ============================================================
# PART 4 — CALCULATING HOW FAR VALUES ARE OUTSIDE THE RANGE
# ============================================================
#
# We can first filter the abnormal values and then perform
# calculations on the filtered array.
#
# For values above 139:
#
# amount above = value - 139


high_bp = bp[bp > 139]

amount_above = high_bp - 139

print("High BP values:", high_bp)
print("Amount above 139:", amount_above)

# Output:
# High BP values: [142 160 148]
# Amount above 139: [ 3 21  9]


# We can do the same for values below 90.


low_bp = bp[bp < 90]

amount_below = 90 - low_bp

print("Low BP values:", low_bp)
print("Amount below 90:", amount_below)

# There are no values below 90 in our dataset.
#
# Output:
# Low BP values: []
# Amount below 90: []


# ============================================================
# PART 5 — SUMMARY STATISTICS
# ============================================================
#
# NumPy provides several functions for summarising numerical
# data.


print("Mean:", np.mean(bp))
print("Maximum:", np.max(bp))
print("Minimum:", np.min(bp))
print("Standard deviation:", np.std(bp))


# Range is not a separate NumPy function.
#
# We calculate it as:
#
# maximum - minimum


print("Range:", np.max(bp) - np.min(bp))

# For this dataset:
#
# Maximum = 160
# Minimum = 110
# Range = 50


# ============================================================
# PART 6 — WORKING WITH 2D ARRAYS
# ============================================================
#
# A 2D array can represent a table.
#
# Each row can represent a patient.
# Each column can represent a measurement.


vitals = np.array([
    [120, 80],
    [140, 90],
    [130, 85],
    [160, 100]
])

print(vitals)

# Column 0 = SBP
# Column 1 = DBP
#
# Each row represents one patient.


# ============================================================
# PART 7 — SELECTING COLUMNS
# ============================================================
#
# To select all rows from column 0:
#
# array[:, 0]
#
# The ":" means all rows.


sbp = vitals[:, 0]
dbp = vitals[:, 1]

print("SBP:", sbp)
print("DBP:", dbp)

# Output:
# SBP: [120 140 130 160]
# DBP: [ 80  90  85 100]


# ============================================================
# PART 8 — AXIS=0
# ============================================================
#
# axis=0 means:
#
# Perform the calculation DOWN the rows.
#
# This gives one result for each column.
#
# Therefore:
#
# axis=0 → one result per column


mean_by_column = np.mean(vitals, axis=0)

print("Mean of each column:", mean_by_column)

# Output:
# Mean of each column: [137.5   88.75]
#
# Mean SBP = 137.5
# Mean DBP = 88.75


# ============================================================
# PART 9 — AXIS=1
# ============================================================
#
# axis=1 means:
#
# Perform the calculation ACROSS each row.
#
# This gives one result for each patient.
#
# Therefore:
#
# axis=1 → one result per row


mean_by_patient = np.mean(vitals, axis=1)

print("Mean of each patient:", mean_by_patient)

# Output:
# Mean of each patient:
# [100.  115.  107.5 130.]


# ============================================================
# AXIS MEMORY TRICK
# ============================================================
#
# axis=0 → DOWN → one result per column
#
# axis=1 → ACROSS → one result per row
#
# Remember:
#
# 0 = down
# 1 = across


# ============================================================
# PART 10 — OTHER STATISTICS WITH AXIS
# ============================================================
#
# The same axis principle works with other NumPy functions.


print("Maximum per patient:", np.max(vitals, axis=1))
print("Minimum per patient:", np.min(vitals, axis=1))
print("Standard deviation per patient:", np.std(vitals, axis=1))

# Example:
#
# np.max(vitals, axis=1)
#
# Output:
# [120 140 130 160]
#
# This finds the highest measurement for each patient.


# ============================================================
# PART 11 — FILTERING ROWS IN A 2D ARRAY
# ============================================================
#
# Suppose we want complete patient rows where:
#
# SBP >= 140
#
# First we select column 0:
#
# vitals[:, 0]
#
# Then we create the condition:
#
# vitals[:, 0] >= 140
#
# Finally, we use that condition to filter the complete array.


high_sbp_patients = vitals[vitals[:, 0] >= 140]

print("Patients with SBP >= 140:")
print(high_sbp_patients)

# Output:
# [[140  90]
#  [160 100]]


# ============================================================
# PART 12 — COUNTING VALUES THAT MEET A CONDITION
# ============================================================
#
# Boolean values can be counted because:
#
# True = 1
# False = 0
#
# Therefore, np.sum() can count how many values satisfy
# a condition.


number_high_sbp = np.sum(vitals[:, 0] >= 140)

print("Number of patients with SBP >= 140:", number_high_sbp)

# Output:
# Number of patients with SBP >= 140: 2


# ============================================================
# PART 13 — COMBINING CONDITIONS
# ============================================================
#
# We can combine multiple conditions.
#
# & means AND
#
# | means OR
#
# Example:
#
# SBP >= 140 AND heart rate > 100
#
# For this example we need a dataset containing heart rate.


patients = np.array([
    [120, 80, 72],
    [140, 90, 85],
    [130, 85, 78],
    [160, 100, 102],
    [125, 82, 70]
])

# Column 0 = SBP
# Column 1 = DBP
# Column 2 = Heart rate


patients_with_both = patients[
    (patients[:, 0] >= 140) &
    (patients[:, 2] > 100)
]

print("Patients with both high SBP and high heart rate:")
print(patients_with_both)

# Output:
# [[160 100 102]]


# ============================================================
# PART 14 — OR CONDITIONS
# ============================================================
#
# We can also find patients who meet either condition.
#
# SBP >= 140 OR heart rate > 100


patients_with_either = patients[
    (patients[:, 0] >= 140) |
    (patients[:, 2] > 100)
]

print("Patients with high SBP OR high heart rate:")
print(patients_with_either)


# ============================================================
# PART 15 — MINI PROJECT
# PATIENT VITAL SIGNS ANALYZER
# ============================================================
#
# We now combine the skills from this lesson into one
# practical healthcare analysis.


patients = np.array([
    [120, 80, 72],
    [140, 90, 85],
    [130, 85, 78],
    [160, 100, 102],
    [125, 82, 70]
])


# ----------------------------
# Mean values
# ----------------------------

print("Mean SBP:", np.mean(patients[:, 0]))
print("Mean DBP:", np.mean(patients[:, 1]))
print("Mean heart rate:", np.mean(patients[:, 2]))

print()


# ----------------------------
# Highest values
# ----------------------------

print("Highest SBP:", np.max(patients[:, 0]))
print("Highest DBP:", np.max(patients[:, 1]))
print("Highest heart rate:", np.max(patients[:, 2]))

print()


# ----------------------------
# Lowest values
# ----------------------------

print("Lowest SBP:", np.min(patients[:, 0]))
print("Lowest DBP:", np.min(patients[:, 1]))
print("Lowest heart rate:", np.min(patients[:, 2]))

print()


# ----------------------------
# Standard deviation
# ----------------------------

print(
    "Standard deviation of SBP:",
    np.std(patients[:, 0])
)

print(
    "Standard deviation of DBP:",
    np.std(patients[:, 1])
)

print(
    "Standard deviation of heart rate:",
    np.std(patients[:, 2])
)

print()


# ----------------------------
# Patients with high SBP
# ----------------------------

high_sbp = patients[patients[:, 0] >= 140]

print("Patients with SBP >= 140:")
print(high_sbp)

print(
    "Number of patients with SBP >= 140:",
    len(high_sbp)
)

print()


# ----------------------------
# Patients with high heart rate
# ----------------------------

high_heart_rate = patients[patients[:, 2] > 100]

print("Patients with heart rate > 100:")
print(high_heart_rate)

print()


# ----------------------------
# Patients with both
# high SBP AND high heart rate
# ----------------------------

patients_with_both = patients[
    (patients[:, 0] >= 140) &
    (patients[:, 2] > 100)
]

print(
    "Patients with both high SBP and high heart rate:"
)

print(patients_with_both)


# ============================================================
# PRACTICE
# ============================================================
#
# These exercises are for future review.
# We completed the main lesson and mini-project together.
#
#
# PRACTICE 1
# ----------
#
# Given:
#
# temperatures = np.array([
#     36.5,
#     37.2,
#     38.1,
#     39.0,
#     36.8,
#     37.8
# ])
#
# Find all temperatures above 38.0.
#
#
# PRACTICE 2
# ----------
#
# Using the same temperature array, calculate:
#
# - Mean
# - Maximum
# - Minimum
# - Standard deviation
# - Range
#
#
# PRACTICE 3
# ----------
#
# Create:
#
# labs = np.array([
#     [5.2, 110],
#     [6.1, 125],
#     [4.8, 98],
#     [7.0, 145]
# ])
#
# Column 0 = Hb
# Column 1 = Glucose
#
# Calculate:
#
# - Mean Hb
# - Mean glucose
# - Highest Hb
# - Highest glucose
# - Lowest Hb
# - Lowest glucose
#
#
# PRACTICE 4
# ----------
#
# Using labs, find patients whose glucose is above 120.


# ============================================================
# KEY TAKEAWAYS
# ============================================================
#
# 1. Boolean conditions can be used to filter NumPy arrays.
#
# 2. Boolean filtering works on both 1D and 2D arrays.
#
# 3. We can filter values and then perform calculations on
#    the filtered results.
#
# 4. np.mean() calculates the mean.
#
# 5. np.max() finds the maximum.
#
# 6. np.min() finds the minimum.
#
# 7. np.std() calculates standard deviation.
#
# 8. Range can be calculated as:
#
#       np.max(array) - np.min(array)
#
# 9. In a 2D array:
#
#       array[:, 0]
#
#    selects column 0.
#
# 10. axis=0 performs calculations down the rows and gives
#     one result per column.
#
# 11. axis=1 performs calculations across the columns and
#     gives one result per row.
#
# 12. & means AND.
#
# 13. | means OR.
#
# 14. When combining conditions, use parentheses around each
#     condition.
#
#
# CORE NUMPY DATA-ANALYSIS PATTERN:
#
# SELECT → FILTER → CALCULATE → SUMMARIZE
#
#
# ============================================================
# LESSON 27 COMPLETE
# ============================================================
#
# Lesson 26 — NumPy Fundamentals       ✓
# Lesson 27 — NumPy in Practice        ✓
#
# Next lesson: Lesson 28
# ============================================================