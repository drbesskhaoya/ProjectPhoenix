# ============================================================
# PROJECT PHOENIX
# WEEK 1 — LESSON 13: FILE HANDLING
# ============================================================
#
# Topics:
# 1. Why file handling is useful
# 2. Opening and closing files
# 3. Write mode ("w")
# 4. New lines with \n
# 5. Read mode ("r")
# 6. Append mode ("a")
# 7. Using with open()
# 8. Reading with .read()
# 9. Reading with .readline()
# 10. Reading with .readlines()
# 11. Reading files with a for loop
# 12. Using .strip() when reading files
# 13. Writing variables and user input to files
# 14. Handling FileNotFoundError
# 15. Mini Project — Patient Record System
#
# ============================================================


# ============================================================
# 1. WHY FILE HANDLING?
# ============================================================

# Variables only exist while a program is running.
#
# Files allow information to remain stored after the program
# has finished.
#
# Examples:
#
# patient.txt
# observations.txt
# appointments.txt
#
# Python can create, write to, read from, and update files.


# ============================================================
# 2. OPENING A FILE
# ============================================================

# Basic syntax:
#
# file = open("filename.txt", "mode")
#
# Common modes:
#
# "w" = write
# "r" = read
# "a" = append


# ============================================================
# 3. WRITE MODE — "w"
# ============================================================

# Write mode creates a file if it does not already exist.
#
# IMPORTANT:
# If the file already exists, "w" replaces its existing
# contents.

file = open("patient.txt", "w")

file.write("Patient: Bessie\n")
file.write("Age: 30\n")
file.write("Diagnosis: Malaria\n")

file.close()


# ============================================================
# 4. NEW LINES — \n
# ============================================================

# file.write() does NOT automatically move to a new line.
#
# Without \n:

# file.write("Patient: James")
# file.write("Age: 45")

# The file would contain:
#
# Patient: JamesAge: 45
#
# Using \n creates separate lines:

file = open("patient.txt", "w")

file.write("Patient: James\n")
file.write("Age: 45\n")

file.close()


# ============================================================
# 5. READ MODE — "r"
# ============================================================

# "r" opens an existing file for reading.

file = open("patient.txt", "r")

content = file.read()

print(content)

file.close()


# ============================================================
# 6. APPEND MODE — "a"
# ============================================================

# Append mode adds information to the END of an existing file.
#
# Unlike "w", it does not erase the existing contents.

file = open("patient.txt", "a")

file.write("Diagnosis: Pneumonia\n")

file.close()


# ============================================================
# 7. USING with open()
# ============================================================

# Instead of manually opening and closing files, Python provides
# the with statement.
#
# Python automatically closes the file when the with block ends.

with open("patient.txt", "r") as file:
    content = file.read()

print(content)

# No file.close() is required.
#
# This is generally the preferred way to work with files.


# ============================================================
# 8. .read()
# ============================================================

# .read() reads the ENTIRE file as one string.

with open("patient.txt", "r") as file:
    content = file.read()

print(content)


# ============================================================
# 9. .readline()
# ============================================================

# .readline() reads ONE line at a time.
#
# Each call continues from where the previous call stopped.

with open("patient.txt", "r") as file:
    patient = file.readline().strip()
    age = file.readline().strip()
    diagnosis = file.readline().strip()

print(patient)
print(age)
print(diagnosis)


# ============================================================
# 10. USING .strip()
# ============================================================

# Lines read from text files often contain \n at the end.
#
# For example:
#
# "Patient: Bessie\n"
#
# .strip() removes leading and trailing whitespace, including
# the newline character.

with open("patient.txt", "r") as file:
    first_line = file.readline().strip()

print(first_line)


# ============================================================
# 11. READING A FILE WITH A for LOOP
# ============================================================

# A for loop is useful when a file contains many lines.
#
# Instead of calling .readline() repeatedly, we can loop
# through the file.

with open("patient.txt", "r") as file:
    for line in file:
        print(line.strip())


# ============================================================
# 12. .readlines()
# ============================================================

# .readlines() reads all lines and returns them as a LIST.
#
# For example, a file containing:
#
# Alice
# Brian
# Catherine
#
# could produce approximately:
#
# ["Alice\n", "Brian\n", "Catherine\n"]

with open("patient.txt", "r") as file:
    lines = file.readlines()

print(lines)
print("Number of lines:", len(lines))


# ============================================================
# 13. WRITING VARIABLES TO A FILE
# ============================================================

patient_name = "John"
patient_age = 42
diagnosis = "Pneumonia"

with open("patient_record.txt", "w") as file:
    file.write(f"Patient Name: {patient_name}\n")
    file.write(f"Age: {patient_age}\n")
    file.write(f"Diagnosis: {diagnosis}\n")


# ============================================================
# 14. SAVING USER INPUT
# ============================================================

# Information entered by the user can be stored permanently
# inside a file.

patient_name = input("Enter patient name: ")
patient_age = int(input("Enter patient age: "))
diagnosis = input("Enter diagnosis: ")

file_name = "patient_record.txt"

with open(file_name, "w") as file:
    file.write(f"Patient Name: {patient_name}\n")
    file.write(f"Age: {patient_age}\n")
    file.write(f"Diagnosis: {diagnosis}\n")


# ============================================================
# 15. HANDLING A MISSING FILE
# ============================================================

# Trying to read a file that does not exist causes:
#
# FileNotFoundError
#
# We can handle this using try and except.
#
# Exception handling will be studied in more detail later.

try:
    with open("missing_patient.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Patient record not found.")


# ============================================================
# PRACTICE — PATIENT OBSERVATIONS
# ============================================================

# Example: write patient observations to a file.

with open("observations.txt", "w") as file:
    file.write("Temperature: 37.2\n")
    file.write("Heart Rate: 80\n")

# Add more observations without deleting the previous ones.

with open("observations.txt", "a") as file:
    file.write("Blood Pressure: 120/80\n")
    file.write("SpO2: 98%\n")

# Read and display the observations.

with open("observations.txt", "r") as file:
    for line in file:
        print(line.strip())


# ============================================================
# MINI PROJECT — PATIENT RECORD SYSTEM
# ============================================================
#
# Goal:
# Create a simple system that:
#
# 1. Collects patient information.
# 2. Saves the patient to a text file.
# 3. Keeps previous patient records.
# 4. Displays all stored records.
#
# Concepts combined:
#
# - input()
# - int()
# - float()
# - variables
# - f-strings
# - with open()
# - append mode
# - read mode
# - .write()
# - .read()


patient_name = input("Enter patient name: ")
patient_age = int(input("Enter patient age: "))
temperature = float(input("Enter patient temperature: "))
diagnosis = input("Enter diagnosis: ")

file_name = "patient_record.txt"


# Save the patient record.
#
# "a" is used so previous patient records are preserved.

with open(file_name, "a") as file:
    file.write(f"Patient Name: {patient_name}\n")
    file.write(f"Age: {patient_age}\n")
    file.write(f"Temperature: {temperature}\n")
    file.write(f"Diagnosis: {diagnosis}\n")
    file.write("-------------------------------\n")


# Display all stored patient records.

print("\nPATIENT RECORDS")
print("===============================")

with open(file_name, "r") as file:
    print(file.read())


# ============================================================
# KEY TAKEAWAYS
# ============================================================
#
# 1. Files allow programs to store information permanently.
#
# 2. open("file.txt", "w")
#    writes to a file and replaces existing contents.
#
# 3. open("file.txt", "r")
#    reads an existing file.
#
# 4. open("file.txt", "a")
#    adds new information without deleting existing information.
#
# 5. \n creates a new line inside a text file.
#
# 6. .read()
#    reads the entire file as one string.
#
# 7. .readline()
#    reads one line at a time.
#
# 8. .readlines()
#    reads all lines into a list.
#
# 9. A for loop can process a file one line at a time.
#
# 10. .strip() is useful for removing newline characters and
#     other surrounding whitespace.
#
# 11. with open() automatically closes the file and is generally
#     preferred over manually calling file.close().
#
# 12. FileNotFoundError occurs when Python tries to read a file
#     that does not exist.
#
# 13. File handling can be combined with variables, input,
#     loops, f-strings, lists, and other Python concepts to build
#     programs that preserve data between runs.
#
# ============================================================
# END OF LESSON 13 — FILE HANDLING
# PROJECT PHOENIX — WEEK 1
# ============================================================