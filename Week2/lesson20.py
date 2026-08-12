# ============================================================
# PROJECT PHOENIX — WEEK 2
# LESSON 20: ENCAPSULATION & ACCESS CONTROL
# ============================================================
#
# Goal:
# Learn how to protect object data and control how it is
# accessed or modified.
#
# Healthcare Focus:
# Protecting patient information and validating healthcare
# data before it enters the system.
#
# ============================================================


# ============================================================
# PART 1 — WHAT IS ENCAPSULATION?
# ============================================================

# Encapsulation means keeping an object's data and the methods
# that control that data together inside the class.
#
# Instead of allowing every part of a program to freely change
# important data, we can control how that data is accessed.
#
# Example:
#
# patient.age = -10
#
# Without validation, Python will allow this.
#
# In a healthcare system, uncontrolled changes can cause
# incorrect or unsafe data to enter the system.


# ============================================================
# PART 2 — THE PROBLEM WITH PUBLIC ATTRIBUTES
# ============================================================

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age


patient1 = Patient("John", 35)

# Python allows us to change the age directly.
patient1.age = -10

print("Patient age:", patient1.age)


# Senior Engineer Note:
#
# Python does not automatically know that -10 is an invalid age.
#
# The class currently gives outside code unrestricted access
# to the attribute.
#
# This can become dangerous when working with:
# - Patient information
# - Medical measurements
# - Medication doses
# - AI predictions
# - Risk scores
# - Billing information


# ============================================================
# PART 3 — SINGLE UNDERSCORE
# ============================================================

class Patient:
    def __init__(self, name, age):
        self.name = name
        self._age = age


patient1 = Patient("John", 35)

print("Patient age:", patient1._age)


# A single underscore is a convention.
#
# _age means:
#
# "This attribute is intended for internal use."
#
# IMPORTANT:
# A single underscore does NOT actually prevent access.
#
# Python still allows:
#
# patient1._age = -10
#
# Therefore, _age is mainly a communication convention
# between developers.


# ============================================================
# PART 4 — DOUBLE UNDERSCORE
# ============================================================

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


patient1 = Patient("John", 35)


# __age uses Python's name-mangling mechanism.
#
# It makes accidental access and name collisions less likely.
#
# IMPORTANT:
# __age is NOT encryption or true security.
#
# Python internally changes the name of the attribute.


# ============================================================
# PART 5 — GETTERS
# ============================================================

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age


patient1 = Patient("John", 35)

print("Patient age:", patient1.get_age())


# A getter is a method used to read internal data.
#
# Instead of:
#
# patient1.__age
#
# we use:
#
# patient1.get_age()
#
# This gives the class control over how the data is accessed.


# ============================================================
# PART 6 — SETTERS
# ============================================================

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age


patient1 = Patient("John", 35)

patient1.set_age(40)

print("Updated age:", patient1.get_age())


# The setter allows us to control changes to the data.
#
# The validation rule prevents invalid values from being stored.
#
# Example:
#
# patient1.set_age(-10)
#
# The condition fails, so the value remains unchanged.


patient1.set_age(-10)

print("Age after invalid update:", patient1.get_age())


# ============================================================
# PART 7 — WHY VALIDATION MATTERS
# ============================================================

# Without validation:

class UnsafePatient:
    def __init__(self, age):
        self.age = age


patient = UnsafePatient(35)

patient.age = -50

print("Unsafe age:", patient.age)


# With controlled access:

class SafePatient:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age


patient = SafePatient(35)

patient.set_age(-50)

print("Safe age:", patient.get_age())


# Healthcare AI Connection:
#
# Validation is extremely important when data will later be
# processed by software or AI.
#
# Invalid input can lead to:
#
# Patient data
#      ↓
# Incorrect value
#      ↓
# AI/system processing
#      ↓
# Incorrect result
#
# Good software design tries to prevent invalid data early.


# ============================================================
# PART 8 — @PROPERTY
# ============================================================

# Python provides a cleaner way to implement controlled access.
#
# We can use @property.


class Patient:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age


patient1 = Patient("John", 35)

print("Patient age:", patient1.age)


# @property allows us to access the method like an attribute:
#
# patient1.age
#
# instead of:
#
# patient1.get_age()
#
# Python automatically calls the property method.


# ============================================================
# PART 9 — @PROPERTY SETTER
# ============================================================

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value


patient1 = Patient("John", 35)

patient1.age = 40

print("Updated age:", patient1.age)


# The following is rejected because age cannot be negative.

patient1.age = -10

print("Age after invalid update:", patient1.age)


# ============================================================
# PART 10 — UNDERSTANDING THE FLOW
# ============================================================

# When we write:
#
# patient1.age
#
# Python uses:
#
# @property
# def age(self):
#     return self.__age
#
#
# When we write:
#
# patient1.age = 40
#
# Python uses:
#
# @age.setter
# def age(self, value):
#     if value >= 0:
#         self.__age = value
#
#
# The flow is:
#
#        patient1.age = 40
#                ↓
#           setter method
#                ↓
#            validation
#                ↓
#        self.__age = 40
#
#
# This gives the class control over its internal data.


# ============================================================
# PART 11 — HEALTHCARE AI EXAMPLE
# ============================================================

class Patient:
    def __init__(self, name, risk_score):
        self.name = name
        self.__risk_score = risk_score

    @property
    def risk_score(self):
        return self.__risk_score

    @risk_score.setter
    def risk_score(self, value):

        if value >= 0 and value <= 100:
            self.__risk_score = value


patient1 = Patient("John", 72)

patient1.risk_score = 85

print("Risk score:", patient1.risk_score)

patient1.risk_score = 150

print("Risk score after invalid update:", patient1.risk_score)


# Expected output:
#
# Risk score: 85
# Risk score after invalid update: 85
#
# 150 is rejected because the allowed range is 0–100.


# Healthcare AI Connection:
#
# Imagine an AI system produces a patient risk score.
#
# A validation layer can help ensure that impossible values
# do not enter the system.
#
# NOTE:
# Real clinical systems require much more sophisticated
# validation and clinical governance.
#
# This example is for learning software design.


# ============================================================
# PART 12 — MINI PROJECT
# PATIENT DATA VALIDATION SYSTEM
# ============================================================

class PatientRecord:
    def __init__(self, name, age, risk_score):
        self.name = name
        self.__age = age
        self.__risk_score = risk_score

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value

    @property
    def risk_score(self):
        return self.__risk_score

    @risk_score.setter
    def risk_score(self, value):
        if value >= 0 and value <= 100:
            self.__risk_score = value


patient = PatientRecord("Alice", 42, 65)

print("\n========== PATIENT RECORD ==========")
print("Name:", patient.name)
print("Age:", patient.age)
print("Risk Score:", patient.risk_score)


# Test valid updates

patient.age = 43
patient.risk_score = 70

print("\n========== AFTER VALID UPDATE ==========")
print("Age:", patient.age)
print("Risk Score:", patient.risk_score)


# Test invalid updates

patient.age = -5
patient.risk_score = 150

print("\n========== AFTER INVALID UPDATE ==========")
print("Age:", patient.age)
print("Risk Score:", patient.risk_score)


# Expected:
#
# The invalid values should NOT replace the valid values.


# ============================================================
# PART 13 — DEBUGGING CHALLENGE
# ============================================================

# Find the mistake in this code:

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.age = value


# Problem:
#
# The setter uses:
#
# self.age = value
#
# instead of:
#
# self.__age = value
#
# This causes the setter to call itself again.
#
# The correct version is:
#
# self.__age = value
#
#
# Senior Engineer Note:
#
# When working with properties, be very careful not to
# accidentally call the property setter from inside itself.


# ============================================================
# PART 14 — COMMON MISTAKES
# ============================================================

# Mistake 1:
#
# self.age = age
#
# when we intended to protect the attribute.
#
# Better:
#
# self.__age = age


# Mistake 2:
#
# Assuming _age is completely private.
#
# It is not.
#
# _age is mainly a developer convention.


# Mistake 3:
#
# Assuming __age provides encryption.
#
# It does not.
#
# It uses name mangling.


# Mistake 4:
#
# Forgetting return in a getter.
#
# Wrong:
#
# def get_age(self):
#     self.__age
#
# Correct:
#
# def get_age(self):
#     return self.__age


# Mistake 5:
#
# Updating the wrong attribute in a setter.
#
# Wrong:
#
# self.age = value
#
# Correct:
#
# self.__age = value


# Mistake 6:
#
# Forgetting validation.
#
# A setter becomes much more useful when it enforces
# meaningful rules.


# ============================================================
# PART 15 — PRACTICE CHALLENGES
# ============================================================

# CHALLENGE 1
#
# Create a Patient class with:
#
# name
# age
#
# Store age using __age.
#
# Create an @property for age.
#
# Create an @age.setter.
#
# Reject negative ages.


# CHALLENGE 2
#
# Add weight to the Patient class.
#
# Store it internally as:
#
# __weight
#
# Only allow weights greater than 0.


# CHALLENGE 3
#
# Add a blood pressure value.
#
# Create validation so that the value cannot be negative.
#
# Think carefully about whether storing systolic and diastolic
# blood pressure as one value or two values makes more sense.


# CHALLENGE 4
#
# Add an AI risk score.
#
# Only allow values from:
#
# 0 to 100


# ============================================================
# PART 16 — SENIOR ENGINEER NOTES
# ============================================================

# 1. Encapsulation is about controlling access to data.
#
# 2. Not every attribute needs to be private.
#
# 3. Do not add complicated protection just because you can.
#
# 4. Use encapsulation when a class needs to enforce rules
#    around its internal state.
#
# 5. Keep validation close to the data it protects.
#
# 6. @property is often cleaner than manually creating
#    get_x() and set_x() methods.
#
# 7. Good object-oriented design protects the integrity
#    of an object's state.
#
# 8. Encapsulation is a design tool, not a substitute for
#    authentication, authorization, encryption, or database
#    security.


# ============================================================
# PART 17 — HEALTHCARE AI CONNECTION
# ============================================================

# Project Phoenix is gradually moving from simple Python
# programs toward software architecture.
#
# In a future healthcare system we may have:
#
# Patient
# Doctor
# Nurse
# Appointment
# MedicalRecord
# LaboratoryResult
# Medication
# AIModel
# RiskPrediction
#
# Each object should be responsible for maintaining valid
# internal state.
#
# Example:
#
# Patient
#    ↓
# Patient data
#    ↓
# Validation
#    ↓
# Medical system
#    ↓
# AI model
#    ↓
# Prediction
#
# Encapsulation helps prevent invalid object state from
# spreading through the rest of the system.


# ============================================================
# PART 18 — KEY TAKEAWAYS
# ============================================================

# 1. Encapsulation means controlling access to an object's data.
#
# 2. Public attributes can be changed directly.
#
# 3. _attribute communicates that an attribute is intended
#    for internal use.
#
# 4. __attribute uses name mangling.
#
# 5. Getters allow controlled reading of internal data.
#
# 6. Setters allow controlled modification of internal data.
#
# 7. @property provides a Pythonic way to create getters.
#
# 8. @property.setter provides a Pythonic way to create setters.
#
# 9. Validation can prevent invalid data from entering an object.
#
# 10. Healthcare systems benefit from carefully controlled
#     patient and clinical data.
#
# 11. Encapsulation is one of the foundations of robust
#     object-oriented software.
#
# ============================================================
# END OF LESSON 20
# ============================================================