
# ============================================================
# PROJECT PHOENIX
# LESSON 12: STRINGS
# ============================================================

# Topics:
# 1. Creating Strings
# 2. String Indexing
# 3. Negative Indexing
# 4. String Slicing
# 5. String Case Methods
# 6. Removing Whitespace
# 7. Replacing Text
# 8. String Immutability
# 9. Finding Text
# 10. Counting Text
# 11. Splitting Strings
# 12. Joining Strings
# 13. Method Chaining
# 14. f-Strings
# 15. Formatting Numbers
# 16. startswith() and endswith()
# 17. Checking Membership with "in"
# 18. Mini Project: Patient Registration & Summary


# ============================================================
# 1. CREATING STRINGS
# ============================================================

# A string is text enclosed in quotation marks.

patient = "John Doe"
hospital = "Avenue Hospital"
diagnosis = "Hypertension"

print(patient)
print(hospital)
print(diagnosis)


# ============================================================
# 2. STRING INDEXING
# ============================================================

# Each character in a string has an index.
# Python indexing starts at 0.

name = "John"

print(name[0])  # J
print(name[1])  # o
print(name[2])  # h
print(name[3])  # n


# ============================================================
# 3. NEGATIVE INDEXING
# ============================================================

# Negative indexes count backwards from the end.
#
# J  o  h  n
# 0  1  2  3
#
# -4 -3 -2 -1

name = "John"

print(name[-1])  # n
print(name[-2])  # h
print(name[-3])  # o
print(name[-4])  # J

hospital = "Avenue Hospital"

print(hospital[0])   # First character: A
print(hospital[-1])  # Last character: l


# ============================================================
# 4. STRING SLICING
# ============================================================

# Slicing extracts part of a string.
#
# Syntax:
#
# string[start:end]
#
# The start index is INCLUDED.
# The end index is EXCLUDED.

hospital = "Avenue Hospital"

print(hospital[0:6])  # Avenue

patient = "John Doe"

print(patient[5:8])   # Doe


# ------------------------------------------------------------
# Omitting the start index
# ------------------------------------------------------------

# Start from the beginning.

print(patient[:4])    # John


# ------------------------------------------------------------
# Omitting the end index
# ------------------------------------------------------------

# Continue to the end.

print(patient[5:])    # Doe


# ------------------------------------------------------------
# Negative slicing
# ------------------------------------------------------------

print(patient[-3:])   # Doe

# Everything except the final character:

print(patient[:-1])   # John Do


# ------------------------------------------------------------
# Reversing a string
# ------------------------------------------------------------

print(patient[::-1])  # eoD nhoJ


# ------------------------------------------------------------
# Healthcare example: Patient ID
# ------------------------------------------------------------

patient_id = "PAT-2026-1045"

print(patient_id[:3])   # PAT
print(patient_id[4:8])  # 2026
print(patient_id[-4:])  # 1045


# ============================================================
# 5. STRING CASE METHODS
# ============================================================

patient = "john doe"

# Convert everything to uppercase.

print(patient.upper())
# JOHN DOE


# Convert everything to lowercase.

print(patient.lower())
# john doe


# Capitalize the first letter of each word.

print(patient.title())
# John Doe


# ------------------------------------------------------------
# Healthcare example
# ------------------------------------------------------------

hospital = "aVeNuE hOsPiTaL"

print(hospital.upper())  # AVENUE HOSPITAL
print(hospital.lower())  # avenue hospital
print(hospital.title())  # Avenue Hospital


# ============================================================
# 6. REMOVING WHITESPACE WITH strip()
# ============================================================

# strip() removes whitespace from the beginning and end
# of a string.

patient = "   John Doe   "

print(patient)
print(patient.strip())


diagnosis = "   Malaria"

print(diagnosis.strip())
# Malaria


# Spaces INSIDE the string are preserved.

hospital = "   Avenue Hospital   "

print(hospital.strip())
# Avenue Hospital


# ------------------------------------------------------------
# Cleaning user input
# ------------------------------------------------------------

# A common pattern is:
#
# patient_name = input("Enter patient name: ").strip()


# ============================================================
# 7. REPLACING TEXT WITH replace()
# ============================================================

diagnosis = "Malaria"

print(diagnosis.replace("Malaria", "Typhoid"))
# Typhoid


insurance = "NHIF"

print(insurance.replace("NHIF", "SHA"))
# SHA


# ------------------------------------------------------------
# Healthcare example
# ------------------------------------------------------------

notes = "Patient referred to OPD."

print(notes.replace("OPD", "Outpatient Department"))

# Patient referred to Outpatient Department.


# ============================================================
# 8. STRINGS ARE IMMUTABLE
# ============================================================

# Strings cannot be modified in place.
#
# String methods such as replace() return a NEW string.

hospital = "Avenue Hospital"

hospital.replace("Hospital", "Clinic")

print(hospital)
# Avenue Hospital


# The new string must be assigned to a variable.

hospital = hospital.replace("Hospital", "Clinic")

print(hospital)
# Avenue Clinic


# ============================================================
# 9. FINDING TEXT WITH find()
# ============================================================

# find() returns the starting index of the first match.

hospital = "Avenue Hospital"

print(hospital.find("Hospital"))
# 7

print(hospital.find("Avenue"))
# 0

print(hospital.find("e"))
# 2


# If the text is not found, find() returns -1.

print(hospital.find("Clinic"))
# -1


# ------------------------------------------------------------
# Healthcare example
# ------------------------------------------------------------

notes = "Patient referred to OPD."

if notes.find("OPD") != -1:
    print("Abbreviation found.")


# ============================================================
# 10. COUNTING TEXT WITH count()
# ============================================================

hospital = "Avenue Hospital"

print(hospital.count("a"))
# 1


diagnosis = "Malaria"

print(diagnosis.count("a"))
# 3


# ------------------------------------------------------------
# Counting separators
# ------------------------------------------------------------

record = "John Doe,35,Male,Hypertension"

print(record.count(","))
# 3


# ------------------------------------------------------------
# Case sensitivity
# ------------------------------------------------------------

notes = "Patient has pain. Pain score 8. Pain worsening."

print(notes.count("Pain"))
print(notes.count("pain"))


# To perform a case-insensitive count:

print(notes.lower().count("pain"))
# 3


# ============================================================
# 11. SPLITTING STRINGS WITH split()
# ============================================================

# split() converts one string into a list.

patient = "John Doe"

names = patient.split()

print(names)
# ['John', 'Doe']


medicine = "Paracetamol 500mg Tablet"

parts = medicine.split()

print(parts)
# ['Paracetamol', '500mg', 'Tablet']


# Individual pieces can be accessed using list indexes.

print(parts[0])  # Paracetamol
print(parts[1])  # 500mg
print(parts[2])  # Tablet


# ------------------------------------------------------------
# Splitting using a separator
# ------------------------------------------------------------

record = "John,35,Male,Hypertension"

data = record.split(",")

print(data)
# ['John', '35', 'Male', 'Hypertension']


print(data[0])  # John
print(data[1])  # 35
print(data[2])  # Male
print(data[3])  # Hypertension


# ============================================================
# 12. JOINING STRINGS WITH join()
# ============================================================

# join() combines multiple strings into one string.

names = ["John", "Doe"]

patient = " ".join(names)

print(patient)
# John Doe


departments = ["OPD", "A&E", "Radiology"]

print(", ".join(departments))
# OPD, A&E, Radiology

print("-".join(departments))
# OPD-A&E-Radiology

print(" | ".join(departments))
# OPD | A&E | Radiology


# ------------------------------------------------------------
# Remember:
#
# split()    String -> List
# join()     List   -> String
# ------------------------------------------------------------


# ============================================================
# 13. METHOD CHAINING
# ============================================================

# Multiple string methods can be used together.

notes = "   Patient has Pain.   "

clean_notes = notes.strip().lower()

print(clean_notes)

# Patient has pain.


# Another common pattern:

patient_name = "   john doe   "

patient_name = patient_name.strip().title()

print(patient_name)
# John Doe


# ============================================================
# 14. F-STRINGS
# ============================================================

# f-strings allow variables to be inserted directly into text.

patient = "John Doe"
age = 35
diagnosis = "Hypertension"

summary = (
    f"{patient} is {age} years old "
    f"and has a diagnosis of {diagnosis}."
)

print(summary)

# John Doe is 35 years old and has a diagnosis of Hypertension.


# ------------------------------------------------------------
# Expressions can also be placed inside {}
# ------------------------------------------------------------

weight = 70
height = 1.75

print(f"BMI: {weight / (height * height)}")


# ============================================================
# 15. FORMATTING NUMBERS IN F-STRINGS
# ============================================================

weight = 70
height = 1.75

bmi = weight / (height * height)

# :.1f means:
# Display a floating-point number to one decimal place.

print(f"BMI: {bmi:.1f}")


temperature = 38.267

print(f"Temperature: {temperature:.1f}°C")

# Temperature: 38.3°C


# ============================================================
# 16. startswith() AND endswith()
# ============================================================

# startswith() checks whether a string begins with
# specific text.

patient_id = "PAT-2026-1045"

print(patient_id.startswith("PAT"))
# True

print(patient_id.startswith("2026"))
# False


# ------------------------------------------------------------
# endswith()
# ------------------------------------------------------------

# endswith() checks whether a string ends with specific text.

filename = "patient_results.pdf"

print(filename.endswith(".pdf"))
# True

print(filename.endswith(".csv"))
# False


# ============================================================
# 17. CHECKING MEMBERSHIP WITH "in"
# ============================================================

# The "in" operator checks whether text exists inside
# another string.
#
# It returns True or False.

notes = "Patient reports fever and headache"

print("fever" in notes)
# True

print("cough" in notes)
# False

print("Fever" in notes)
# False


# Python strings are case-sensitive.


# ------------------------------------------------------------
# Comparing find(), count(), and in
# ------------------------------------------------------------

# find()
# Question: WHERE is the text?
# Result: index or -1

# count()
# Question: HOW MANY times does the text appear?
# Result: integer

# in
# Question: IS the text present?
# Result: True or False


# ============================================================
# PRACTICE
# ============================================================

# Practice 1:
# Create a string containing a hospital name.
# Print the first and last characters.


# Practice 2:
# Create:
#
# patient = "John Doe"
#
# Use slicing to print only "John".


# Practice 3:
# Create:
#
# patient_id = "PAT-2026-1045"
#
# Extract:
# PAT
# 2026
# 1045


# Practice 4:
# Clean the following patient name:
#
# "   jOhN dOE   "
#
# Expected result:
# John Doe


# Practice 5:
# Split:
#
# "Amoxicillin 500mg Capsule"
#
# into a list containing the drug name, strength,
# and dosage form.


# Practice 6:
# Join:
#
# ["OPD", "A&E", "Radiology"]
#
# using " | " as the separator.


# ============================================================
# MINI PROJECT
# PATIENT REGISTRATION & SUMMARY
# ============================================================

# This project:
#
# - Collects patient information
# - Removes unwanted spaces
# - Standardizes text
# - Validates the patient ID prefix
# - Converts temperature to a float
# - Formats temperature to one decimal place
# - Produces a formatted patient summary


patient_name = input("Enter patient name: ").strip().title()

patient_id = input("Patient ID: ").strip().upper()

valid_patient_id = patient_id.startswith("PAT")

diagnosis = input("Diagnosis: ").strip().title()

temperature = float(input("Temperature: "))


print()
print("---- PATIENT SUMMARY ----")

print(f"Name: {patient_name}")
print(f"Patient ID: {patient_id}")
print(f"Valid Patient ID: {valid_patient_id}")
print(f"Diagnosis: {diagnosis}")
print(f"Temperature: {temperature:.1f}°C")


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. Strings store text in Python.
#
# 2. String indexes start at 0.
#
# 3. Negative indexes count backwards from the end.
#
# 4. Slicing uses:
#
#       string[start:end]
#
#    The start is included.
#    The end is excluded.
#
# 5. Useful case methods:
#
#       .upper()
#       .lower()
#       .title()
#
# 6. strip() removes leading and trailing whitespace.
#
# 7. replace() returns a new string with text replaced.
#
# 8. Strings are immutable.
#
# 9. find() returns the index of the first match,
#    or -1 if no match exists.
#
# 10. count() counts occurrences.
#
# 11. split() converts a string into a list.
#
# 12. join() combines strings into one string.
#
# 13. String methods can be chained:
#
#       input("Name: ").strip().title()
#
# 14. f-strings insert variables into formatted text:
#
#       f"Patient: {patient}"
#
# 15. Numbers can be formatted:
#
#       f"{temperature:.1f}"
#
# 16. startswith() and endswith() return True or False.
#
# 17. The "in" operator checks whether text exists
#     inside another string.
#
# 18. Python strings are case-sensitive.


# ============================================================
# END OF LESSON 12
# PROJECT PHOENIX
# ============================================================
