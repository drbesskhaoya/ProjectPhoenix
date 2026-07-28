# ============================================================
# PROJECT PHOENIX
# WEEK 2 - LESSON 14: ERROR & EXCEPTION HANDLING
# ============================================================
#
# TOPICS
# ------------------------------------------------------------
# 1. What are exceptions?
# 2. try and except
# 3. Handling specific exceptions
# 4. Multiple except blocks
# 5. else
# 6. finally
# 7. Accessing exception information with "as"
# 8. Raising exceptions with raise
# 9. Exception
# 10. Validating data before calculations
# 11. Exception handling with files
# 12. Mini Project - Patient Admission Validator
#
# ============================================================


# ============================================================
# 1. EXCEPTIONS
# ============================================================

# A syntax error occurs when Python cannot understand the code.
#
# Example:
#
# if age > 18
#     print("Adult")
#
# The missing colon causes a SyntaxError.
#
#
# An exception occurs while a program is running.
#
# Example:
#
# age = int("twenty")
#
# "twenty" cannot be converted into an integer.
# Python raises a ValueError.


# ============================================================
# 2. TRY AND EXCEPT
# ============================================================

# try contains code that might cause an exception.
# except tells Python what to do if that exception occurs.

try:
    age = int(input("Enter patient age: "))
    print(f"Patient age: {age}")

except ValueError:
    print("Invalid age. Please enter a whole number.")


# Basic structure:
#
# try:
#     risky code
#
# except SomeError:
#     handle the error


# ============================================================
# 3. HANDLING SPECIFIC EXCEPTIONS
# ============================================================

# Different problems produce different exceptions.
#
# ValueError:
# Occurs when a value is inappropriate for an operation.
#
# Example:
# int("twenty")
#
#
# ZeroDivisionError:
# Occurs when attempting to divide by zero.
#
# Example:
# 10 / 0


try:
    number_of_patients = int(input("Enter number of patients: "))
    number_of_nurses = int(input("Enter number of nurses: "))

    patients_per_nurse = number_of_patients / number_of_nurses

    print(f"Each nurse will take care of {patients_per_nurse} patients.")

except ZeroDivisionError:
    print("Error: Number of nurses cannot be zero.")


# ============================================================
# 4. MULTIPLE EXCEPT BLOCKS
# ============================================================

# One try block can have several except blocks.
#
# This allows different exceptions to be handled differently.

try:
    number_of_patients = int(input("Enter number of patients: "))
    number_of_nurses = int(input("Enter number of nurses: "))

    patients_per_nurse = number_of_patients / number_of_nurses

    print(f"Patients per nurse: {patients_per_nurse}")

except ValueError:
    print("Error: Please enter whole numbers.")

except ZeroDivisionError:
    print("Error: Number of nurses cannot be zero.")


# ============================================================
# 5. ELSE
# ============================================================

# With try/except, else runs only when NO exception occurs.

try:
    number_of_patients = int(input("Enter number of patients: "))
    number_of_nurses = int(input("Enter number of nurses: "))

    patients_per_nurse = number_of_patients / number_of_nurses

except ValueError:
    print("Error: Please enter whole numbers.")

except ZeroDivisionError:
    print("Error: Number of nurses cannot be zero.")

else:
    print(f"Patients per nurse: {patients_per_nurse}")


# Flow:
#
# try
#  |
#  |-- exception occurs --> matching except
#  |
#  |-- no exception ------> else


# ============================================================
# 6. FINALLY
# ============================================================

# finally runs whether an exception occurs or not.

try:
    patient_id = int(input("Enter patient ID: "))

except ValueError:
    print("Invalid patient ID.")

else:
    print(f"Patient ID {patient_id} accepted.")

finally:
    print("Patient ID check complete.")


# Structure:
#
# try:
#     code that might fail
#
# except:
#     runs if an exception occurs
#
# else:
#     runs if no exception occurs
#
# finally:
#     always runs


# ============================================================
# 7. ACCESSING EXCEPTION INFORMATION
# ============================================================

# We can store information about an exception in a variable.

try:
    temperature = float(input("Enter temperature: "))

except ValueError as error:
    print(f"Invalid temperature: {error}")


# A common shorter variable name is "e".

try:
    age = int(input("Enter patient age: "))

except ValueError as e:
    print(f"Invalid age: {e}")


# ============================================================
# 8. RAISING OUR OWN EXCEPTIONS
# ============================================================

# Sometimes Python accepts a value that is technically valid,
# but the value does not make sense for our program.
#
# Example:
#
# -10 is a valid integer.
#
# But a patient age of -10 is not valid.
#
# We can deliberately raise an exception using "raise".


try:
    age = int(input("Enter patient age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError as e:
    print(f"Invalid age: {e}")

else:
    print(f"Patient age: {age}")


# ============================================================
# 9. GENERAL EXCEPTION HANDLING
# ============================================================

# Exception can catch many common exceptions.
#
# However, specific exceptions should normally be handled first.

try:
    number_of_patients = int(input("Enter number of patients: "))
    number_of_nurses = int(input("Enter number of nurses: "))

    patients_per_nurse = number_of_patients / number_of_nurses

except ValueError:
    print("Please enter whole numbers.")

except ZeroDivisionError:
    print("Number of nurses cannot be zero.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    print(f"Patients per nurse: {patients_per_nurse}")


# Good practice:
#
# Specific exceptions first.
# General Exception last.


# ============================================================
# 10. VALIDATE BEFORE CALCULATING
# ============================================================

# Data should be validated BEFORE calculations are performed.
#
# This prevents avoidable errors.


try:
    weight = float(input("Enter patient weight (kg): "))
    height = float(input("Enter patient height (m): "))

    if weight <= 0 or height <= 0:
        raise ValueError(
            "Weight and height must be greater than zero."
        )

    bmi = weight / (height ** 2)

except ValueError as e:
    print(f"Invalid input: {e}")

else:
    print(f"Patient BMI: {bmi:.1f}")

finally:
    print("BMI calculation completed.")


# Correct order:
#
# 1. Get input
# 2. Validate input
# 3. Perform calculation
# 4. Display result


# ============================================================
# 11. EXCEPTION HANDLING WITH FILES
# ============================================================

# Connection to Lesson 13 - File Handling.
#
# Attempting to open a file that does not exist can raise:
#
# FileNotFoundError


file = None

try:
    file = open("patient.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("Patient file not found.")

finally:
    if file:
        file.close()

    print("File operation complete.")


# Note:
# The "with open(...)" pattern learned in file handling is usually
# preferred because it automatically closes the file.
#
# This example demonstrates how finally can be used for cleanup.


# ============================================================
# PRACTICE: PATIENT AGE VALIDATOR
# ============================================================

try:
    age = int(input("Enter patient age: "))

    if age < 0:
        raise ValueError("Age cannot be less than zero.")

    elif age > 120:
        raise ValueError("Age is outside the expected range.")

except ValueError as e:
    print(f"Invalid age: {e}")

else:
    print(f"Patient age: {age}")

finally:
    print("Age validation complete.")


# ============================================================
# MINI PROJECT: PATIENT ADMISSION VALIDATOR
# ============================================================

# This project combines:
#
# - input()
# - variables
# - type conversion
# - string methods
# - conditionals
# - try
# - except
# - else
# - finally
# - raise
# - ValueError
# - f-strings


try:
    name = input("Enter patient name: ").strip().title()
    age = int(input("Enter patient age: "))
    temperature = float(input("Enter patient temperature (°C): "))

    # Validate patient name
    if not name:
        raise ValueError("Patient name cannot be empty.")

    # Validate age
    if age < 0:
        raise ValueError("Age cannot be less than zero.")

    elif age > 120:
        raise ValueError("Age is outside the expected range.")

    # Validate temperature
    if temperature < 25:
        raise ValueError("Temperature is too low.")

    elif temperature > 45:
        raise ValueError("Temperature is too high.")

except ValueError as e:
    print(f"Invalid input: {e}")

else:
    print("\n--- PATIENT ADMISSION ---")
    print(f"Patient name: {name}")
    print(f"Patient age: {age}")
    print(f"Patient temperature: {temperature}°C")

finally:
    print("Patient admission validation complete.")


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. Exceptions are errors that occur while a program is running.
#
# 2. try contains code that might cause an exception.
#
# 3. except handles an exception instead of allowing the program
#    to crash immediately.
#
# 4. Different exceptions can be handled separately.
#
#    Examples:
#    ValueError
#    ZeroDivisionError
#    FileNotFoundError
#
# 5. else runs when the try block completes without an exception.
#
# 6. finally runs whether an exception occurs or not.
#
# 7. "except ValueError as e" gives access to information about
#    the exception.
#
# 8. raise allows us to deliberately create an exception when
#    data violates the rules of our program.
#
# 9. Validate data BEFORE performing calculations.
#
# 10. Catch specific exceptions whenever possible.
#
#     Prefer:
#
#     except ValueError:
#
#     over blindly catching:
#
#     except Exception:
#
# 11. General Exception handlers should normally come after
#     specific exception handlers.
#
# 12. Exception handling makes programs safer, clearer, and more
#     resilient to invalid input and unexpected situations.


# ============================================================
# END OF LESSON 14
# ============================================================