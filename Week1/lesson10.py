# ============================================

# PROJECT PHOENIX

# Lesson 10 – Dictionaries

# ============================================

"""
TOPICS COVERED

1. What is a dictionary?
2. Creating dictionaries
3. Accessing values
4. Adding new items
5. Updating values
6. Removing items
7. Dictionary methods

   * keys()
   * values()
   * items()
   * get()
8. Looping through dictionaries
9. Mini Project
10. Key Takeaways
    """

# ============================================

# 1. WHAT IS A DICTIONARY?

# ============================================

"""
A dictionary stores data as KEY : VALUE pairs.

Example:

Name ---------> Alice
Age ----------> 27
Blood Group --> A+

Unlike lists, dictionaries allow us to retrieve data using a key instead of
a numerical position.

Lists:
["Alice", 27, "A+"]

Dictionary:
{
"name": "Alice",
"age": 27,
"blood_group": "A+"
}
"""

# ============================================

# 2. CREATING A DICTIONARY

# ============================================

patient = {
"name": "Alice",
"age": 27,
"blood_group": "A+"
}

print(patient)

# ============================================

# 3. ACCESSING VALUES

# ============================================

print(patient["name"])
print(patient["age"])

# ============================================

# 4. ADDING NEW ITEMS

# ============================================

patient["temperature"] = 38.5
patient["pulse"] = 88

print(patient)

# ============================================

# 5. UPDATING VALUES

# ============================================

patient["age"] = 28
patient["temperature"] = 37.2

print(patient)

# ============================================

# 6. REMOVING ITEMS

# ============================================

patient.pop("blood_group")

print(patient)

# ============================================

# 7. DICTIONARY METHODS

# ============================================

patient = {
"name": "Alice",
"age": 27,
"blood_group": "A+"
}

# keys()

print(patient.keys())

# values()

print(patient.values())

# items()

print(patient.items())

# get()

print(patient.get("blood_group"))

# Missing key

print(patient.get("allergy"))

# Missing key with default value

print(patient.get("allergy", "No allergy recorded"))

# ============================================

# 8. LOOPING THROUGH DICTIONARIES

# ============================================

# Loop through keys

for key in patient:
print(key)

print()

# Loop through values

for value in patient.values():
print(value)

print()

# Loop through both keys and values

for key, value in patient.items():
print(f"{key}: {value}")

# ============================================

# MINI PROJECT

# Patient Record Viewer

# ============================================

print()
print("----------- PATIENT RECORD -----------")

patient = {
"Name": "John Doe",
"Age": 45,
"Blood Group": "O+"
}

# Add new information

patient["Temperature"] = 38.2

# Update existing information

patient["Age"] = 28

# Remove information

patient.pop("Blood Group")

# Display patient record

for key, value in patient.items():
print(f"{key}: {value}")

# Display allergy safely

print("Allergies:", patient.get("Allergies", "No allergies reported"))

print("--------------------------------------")

# ============================================

# KEY TAKEAWAYS

# ============================================

"""

1. Dictionaries store information as key-value pairs.

2. Curly braces {} create dictionaries.

3. Access values using:
   dictionary["key"]

4. Add new items using:
   dictionary["new_key"] = value

5. Update values the same way:
   dictionary["key"] = new_value

6. Remove items using:
   dictionary.pop("key")

7. Useful methods:
   keys()
   values()
   items()
   get()

8. get() is safer than [] because it does not raise a KeyError if the key
   does not exist.

9. Loop through dictionaries using:

   for key, value in dictionary.items():
   print(key, value)

10. Dictionaries are ideal for storing structured information such as
    patient records, employee details, student information, or product data.


"""
