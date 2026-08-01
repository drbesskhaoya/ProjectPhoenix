"""
===========================================================
Project Phoenix – Week 2
Lesson 15 – File Handling
===========================================================

Topics Covered
--------------
1. Opening files
2. Reading files
3. Writing files
4. File modes (r, w, a)
5. Using with open()
6. Reading and writing patient records
7. Combining file handling with exception handling

Author: Bessie K
Project: Project Phoenix
"""

# ==========================================================
# PART 1 – OPENING A FILE
# ==========================================================

print("========== PART 1 ==========")

# Read an existing file
with open("patients.txt", "r") as file:
    data = file.read()

print(data)


# ==========================================================
# PART 2 – WRITING TO A FILE
# ==========================================================

print("\n========== PART 2 ==========")

name = input("Enter patient name: ")
age = input("Enter patient age: ")

with open("patients.txt", "a") as file:
    file.write(f"Patient name: {name}, Age: {age}\n")

print("Patient saved successfully.")


# ==========================================================
# PART 3 – DISPLAY ALL RECORDS
# ==========================================================

print("\n========== PART 3 ==========")

print("Current Patient Records")

with open("patients.txt", "r") as file:
    print(file.read())


# ==========================================================
# PART 4 – EXCEPTION HANDLING
# ==========================================================

print("\n========== PART 4 ==========")

try:
    age = int(input("Enter patient age: "))
    print("Age accepted.")

except ValueError:
    print("Invalid age. Please enter numbers only.")


# ==========================================================
# PART 5 – MULTIPLE PATIENTS
# ==========================================================

print("\n========== PART 5 ==========")

while True:

    name = input("Enter patient name (or 'q' to quit): ")

    if name.lower() == "q":
        break

    try:

        age = int(input("Enter patient age: "))

        with open("patients.txt", "a") as file:
            file.write(f"Patient name: {name}, Age: {age}\n")

        print("Patient saved successfully.")

    except ValueError:
        print("Invalid age.")

print("\nAll patients have been saved.")


# ==========================================================
# LESSON SUMMARY
# ==========================================================

print("\n========== LESSON SUMMARY ==========")

print("""
File Modes
----------
r  -> Read a file
w  -> Write (overwrite)
a  -> Append to end of file

Important Methods
-----------------
file.read()
file.write()

Best Practice
-------------
Always use:

with open(...) as file:

instead of:

file = open(...)
file.close()

Python automatically closes the file.

Healthcare Example
------------------
A patient register can be stored in a text file.
Each new patient is appended without deleting
existing records.

Key Takeaways
-------------
✓ Read files using read()
✓ Write files using write()
✓ Understand r, w and a modes
✓ Use with open() instead of open()/close()
✓ Combine file handling with try/except
✓ Build simple persistent applications
""")