# ============================================================
# PROJECT PHOENIX
# LESSON 11: TUPLES AND SETS
# ============================================================

# Topics:
# 1. What is a Tuple?
# 2. Creating Tuples
# 3. Accessing Tuple Items
# 4. Negative Indexing
# 5. Tuple Immutability
# 6. Tuple Length
# 7. Tuple Methods: count() and index()
# 8. Tuple Unpacking
# 9. What is a Set?
# 10. Creating Sets
# 11. Duplicate Values in Sets
# 12. Adding Items with add()
# 13. Removing Items with remove() and discard()
# 14. Set Operations
#     - Union
#     - Intersection
#     - Difference
# 15. Mini Project: Hospital Patient Tracker
# 16. Bonus: The \n Newline Character


# ============================================================
# PART 1: TUPLES
# ============================================================

# A tuple is a collection used to store multiple values.
#
# Tuples use parentheses: ()
#
# Unlike lists, tuples are immutable.
# This means their values cannot be changed after creation.


# ------------------------------------------------------------
# 1. CREATING A TUPLE
# ------------------------------------------------------------

blood_groups = ("A", "B", "AB", "O")

print("Blood groups:")
print(blood_groups)


# A tuple can contain different data types.

patient = ("John", 34, "Male")

print("Patient tuple:")
print(patient)


# ============================================================
# 2. ACCESSING TUPLE ITEMS
# ============================================================

# Tuple indexing starts at 0.

blood_groups = ("A", "B", "AB", "O")

print("First blood group:")
print(blood_groups[0])

print("Third blood group:")
print(blood_groups[2])


# ============================================================
# 3. NEGATIVE INDEXING
# ============================================================

# Negative indexing accesses items starting from the end.
#
# -1 = last item
# -2 = second-last item

blood_groups = ("A", "B", "AB", "O")

print("Last blood group:")
print(blood_groups[-1])


# ============================================================
# 4. TUPLES ARE IMMUTABLE
# ============================================================

# Tuples cannot be changed after they are created.
#
# The following code would produce a TypeError:
#
# blood_groups[0] = "X"
#
# Error:
# TypeError: 'tuple' object does not support item assignment


# ============================================================
# 5. TUPLE LENGTH
# ============================================================

# len() tells us how many items are in a tuple.

blood_groups = ("A", "B", "AB", "O")

print("Number of blood groups:")
print(len(blood_groups))


# ============================================================
# 6. TUPLE METHOD: count()
# ============================================================

# count() tells us how many times a value appears.

blood_groups = ("A", "B", "AB", "O", "A", "A")

print("Number of times A appears:")
print(blood_groups.count("A"))


# ============================================================
# 7. TUPLE METHOD: index()
# ============================================================

# index() returns the index position of the first matching item.

blood_groups = ("A", "B", "AB", "O", "A", "A")

print("Index position of AB:")
print(blood_groups.index("AB"))


# ============================================================
# 8. TUPLE UNPACKING
# ============================================================

# Tuple unpacking allows us to assign tuple values
# directly to separate variables.

patient = ("John", 34, "Male")

name, age, gender = patient

print("Name:", name)
print("Age:", age)
print("Gender:", gender)


# The number of variables must normally match
# the number of values in the tuple.
#
# Example that would cause an error:
#
# patient = ("John", 34, "Male")
# name, age = patient
#
# This produces:
# ValueError: too many values to unpack


# ------------------------------------------------------------
# IGNORING A VALUE DURING UNPACKING
# ------------------------------------------------------------

# An underscore (_) is commonly used when we do not
# need one of the values.

patient = ("John", 34, "Male")

name, age, _ = patient

print("Name:", name)
print("Age:", age)


# ============================================================
# PART 2: SETS
# ============================================================

# A set is another Python collection.
#
# Sets:
# - Use curly braces {}
# - Contain unique values
# - Do not allow duplicates
# - Are unordered
# - Can be modified


# ============================================================
# 9. CREATING A SET
# ============================================================

blood_groups = {"A", "B", "AB", "O"}

print("Blood group set:")
print(blood_groups)


# IMPORTANT:
#
# Sets are unordered.
#
# Python may display the items in a different order.
# Never rely on the order of items inside a set.


# ============================================================
# 10. SETS DO NOT ALLOW DUPLICATES
# ============================================================

patients = {"John", "Mary", "John", "James", "Mary"}

print("Unique patients:")
print(patients)


# Even though John and Mary were entered more than once,
# each name appears only once in the set.


# Healthcare example:

blood_groups = {"A", "O", "A", "AB", "O", "B"}

print("Unique blood groups:")
print(blood_groups)


# ============================================================
# 11. ADDING ITEMS TO A SET
# ============================================================

# add() adds one item to a set.

blood_groups = {"A", "B", "AB"}

blood_groups.add("O")

print("Blood groups after adding O:")
print(blood_groups)


# ------------------------------------------------------------
# ADDING A DUPLICATE
# ------------------------------------------------------------

# Adding an item that already exists does not create
# another copy.

blood_groups = {"A", "B", "AB"}

blood_groups.add("A")

print("Set after trying to add A again:")
print(blood_groups)


# ============================================================
# 12. REMOVING ITEMS: remove()
# ============================================================

blood_groups = {"A", "B", "AB", "O"}

blood_groups.remove("AB")

print("After removing AB:")
print(blood_groups)


# IMPORTANT:
#
# remove() produces an error if the item does not exist.
#
# Example:
#
# blood_groups.remove("X")
#
# This would produce:
# KeyError: 'X'


# ============================================================
# 13. REMOVING ITEMS: discard()
# ============================================================

# discard() also removes an item.
#
# However, if the item does not exist,
# discard() does NOT produce an error.

blood_groups = {"A", "B", "AB", "O"}

blood_groups.discard("X")

print("After discarding X:")
print(blood_groups)


# ------------------------------------------------------------
# remove() VS discard()
# ------------------------------------------------------------

# remove()
# - Removes the item if it exists.
# - Produces a KeyError if it does not exist.
#
# discard()
# - Removes the item if it exists.
# - Does nothing if it does not exist.


# ============================================================
# PART 3: SET OPERATIONS
# ============================================================

doctor_a = {"John", "Mary", "James"}
doctor_b = {"Mary", "James", "Sarah"}


# ============================================================
# 14. UNION
# ============================================================

# The union operator | combines all unique items
# from both sets.

all_patients = doctor_a | doctor_b

print("All unique patients:")
print(all_patients)


# Result contains:
# John, Mary, James and Sarah
#
# The order may vary because sets are unordered.


# ============================================================
# 15. INTERSECTION
# ============================================================

# The intersection operator & finds items that
# appear in BOTH sets.

common_patients = doctor_a & doctor_b

print("Patients seen by both doctors:")
print(common_patients)


# Mary and James appear in both sets.


# ============================================================
# 16. DIFFERENCE
# ============================================================

# The difference operator - finds items in the first
# set that are NOT in the second set.

only_doctor_a = doctor_a - doctor_b

print("Patients seen only by Doctor A:")
print(only_doctor_a)


# John is in Doctor A's set but not Doctor B's set.


# ============================================================
# HEALTHCARE SET OPERATIONS EXAMPLE
# ============================================================

ward_a = {"John", "Mary", "James"}
ward_b = {"James", "Sarah", "Peter"}

all_ward_patients = ward_a | ward_b
patients_in_both = ward_a & ward_b
only_ward_a = ward_a - ward_b

print("All unique ward patients:")
print(all_ward_patients)

print("Patients in both wards:")
print(patients_in_both)

print("Patients only in Ward A:")
print(only_ward_a)


# ============================================================
# MINI PROJECT: HOSPITAL PATIENT TRACKER
# ============================================================

# This mini project combines tuples and sets.
#
# The tuple stores patient information.
# The sets store departments associated with different visits.


# ------------------------------------------------------------
# PATIENT INFORMATION
# ------------------------------------------------------------

patient = ("John", 35, "A+")

name = "Patient Name: " + patient[0]
age = "Age: " + str(patient[1])
blood_group = "Blood Group: " + patient[2]

print(name)
print(age)
print(blood_group)


# ------------------------------------------------------------
# DEPARTMENT VISITS
# ------------------------------------------------------------

morning_shift = {"Emergency", "Radiology", "Laboratory"}
afternoon_shift = {"Laboratory", "Radiology", "Pharmacy"}


# All unique departments visited

all_departments = morning_shift | afternoon_shift


# Departments appearing in both sets

common_departments = morning_shift & afternoon_shift


# Departments visited only during the morning

departments_visited_only_in_morning = morning_shift - afternoon_shift


print("All departments visited:", all_departments)
print("Common departments visited:", common_departments)
print(
    "Departments visited only in the morning:",
    departments_visited_only_in_morning
)


# ============================================================
# BONUS: THE \n NEWLINE CHARACTER
# ============================================================

# \n means "new line".
#
# It can be used inside a string to move the following
# text onto a new line.

print("Hello\nWorld")


# It can also make program output easier to read.

print("\nPATIENT SUMMARY")
print("Patient Name:", patient[0])
print("Age:", patient[1])
print("Blood Group:", patient[2])


# ============================================================
# PRACTICE
# ============================================================

# PRACTICE 1:
# Create a tuple containing:
# patient name, age and blood group.
#
# Access and print each value.


# PRACTICE 2:
# Create a set containing several hospital departments.
# Add another department using add().


# PRACTICE 3:
# Create two sets of patient names.
#
# Find:
# - All unique patients
# - Patients in both sets
# - Patients only in the first set


# PRACTICE 4:
# Create a set with duplicate values.
# Print the set and observe what Python does.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. Tuples use parentheses ().
#
# 2. Tuples are immutable.
#    Their values cannot be changed after creation.
#
# 3. Tuple items can be accessed using indexes.
#
# 4. Negative indexes access tuple items from the end.
#
# 5. len() returns the number of items in a tuple.
#
# 6. count() counts how many times a value occurs.
#
# 7. index() returns the position of the first matching value.
#
# 8. Tuple unpacking assigns tuple values to variables.
#
# 9. Sets use curly braces {}.
#
# 10. Sets contain unique values and automatically
#     eliminate duplicates.
#
# 11. Sets are unordered.
#     Never rely on their printed order.
#
# 12. add() adds an item to a set.
#
# 13. remove() removes an item but raises an error
#     if the item does not exist.
#
# 14. discard() removes an item without raising an error
#     if the item does not exist.
#
# 15. Union | combines all unique items from two sets.
#
# 16. Intersection & finds items shared by two sets.
#
# 17. Difference - finds items in the first set that
#     are not in the second set.
#
# 18. \n is an escape sequence that creates a new line.


# ============================================================
# END OF LESSON 11
# TUPLES AND SETS
# ============================================================
