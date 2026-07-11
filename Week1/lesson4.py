# ==========================================================
# Lesson 4 - User Input and Output

# Topics:
# 1. Getting input from the user
# 2. Storing information in variables
# 3. Displaying formatted output
# ==========================================================


# ==========================================================
# EXERCISE 1 - PERSONAL INFORMATION
# ==========================================================

name = input("What is your name? ")
age = input("What is your age? ")
profession = input("What is your profession? ")

print()

print("Hello,", name)
print("Age:", age, "years")
print("Profession:", profession)

print()


# ==========================================================
# MINI PROJECT
# Simple Patient Registration
# ==========================================================

patient_name = input("Enter patient name: ")
patient_age = int(input("Enter patient age: "))
chief_complaint = input("Chief complaint: ")

print()
print("=" * 35)
print("PATIENT REGISTRATION")
print("=" * 35)

print("Name :", patient_name)
print("Age  :", patient_age, "years")
print("Complaint :", chief_complaint)

print()
print("Registration Complete.")