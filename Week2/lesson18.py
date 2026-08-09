# ============================================================
# PROJECT PHOENIX - WEEK 2
# LESSON 18: OBJECT-ORIENTED PROGRAMMING (OOP)
# ============================================================
#
# Goal:
# Learn how to use Object-Oriented Programming to model
# real-world healthcare entities such as Patients, Doctors,
# Appointments, Prescriptions, and Laboratory Tests.
#
# Project Phoenix Direction:
# Build the foundation for a larger Hospital Management System.
#
# ============================================================


# ============================================================
# PART 1 - WHAT IS OBJECT-ORIENTED PROGRAMMING?
# ============================================================

# Object-Oriented Programming (OOP) is a way of organizing
# programs around OBJECTS.
#
# An object represents a real-world or logical entity.
#
# Healthcare examples:
#
# Patient
# Doctor
# Appointment
# Prescription
# Medication
# Laboratory Test
# Hospital
# Invoice
#
# OOP combines:
#
# DATA       -> Attributes
# BEHAVIOUR  -> Methods
#
# Example:
#
# A Patient has:
#   name
#   age
#   blood_group
#   weight
#   height
#
# A Patient can:
#   calculate BMI
#   update weight
#   display a summary
#
#
# SENIOR ENGINEER NOTE:
# OOP becomes especially useful when software becomes large.
# Instead of managing thousands of unrelated variables and
# functions, we organize related data and behaviour together.
#
#
# HEALTHCARE AI CONNECTION:
# Healthcare systems contain many structured entities.
# OOP provides a way to represent those entities in software
# before connecting them to databases, APIs, ML models,
# LLMs, and clinical decision-support systems.


# ============================================================
# PART 2 - CLASSES
# ============================================================

# A CLASS is a blueprint for creating objects.
#
# Think:
#
# CLASS = Blueprint
# OBJECT = Actual thing created from the blueprint
#
#
# Example:
#
# class Patient:
#     pass
#
# This creates a Patient blueprint.
#
# No actual patient exists yet.


class Patient:
    pass


# ============================================================
# PART 3 - OBJECTS
# ============================================================

# An OBJECT is an actual instance created from a class.
#
# Example:
#
# patient1 = Patient()
#
# Patient = blueprint
# patient1 = actual object


patient1 = Patient()


# We can create another object from the same class:

patient2 = Patient()


# Both objects come from the same blueprint.


# ============================================================
# PART 4 - ATTRIBUTES
# ============================================================

# Attributes are pieces of data belonging to an object.
#
# Example:
#
# patient1.name
# patient1.age
#
# We can assign attributes to an object:

patient1.name = "John"
patient1.age = 42

patient2.name = "Mary"
patient2.age = 35

print("\n========== PART 4: ATTRIBUTES ==========")
print(patient1.name)
print(patient1.age)

print(patient2.name)
print(patient2.age)


# Each object has its own data.
#
# patient1:
#   name -> John
#   age  -> 42
#
# patient2:
#   name -> Mary
#   age  -> 35


# ============================================================
# PART 5 - THE __init__ CONSTRUCTOR
# ============================================================

# Manually assigning attributes becomes repetitive.
#
# Instead of:
#
# patient1 = Patient()
# patient1.name = "John"
# patient1.age = 42
#
# We can use __init__ to automatically initialise an object.
#
# __init__ runs automatically when a new object is created.
#
#
# Example:
#
# def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#
# Then:
#
# patient1 = Patient("John", 42)
#
# Python automatically calls __init__.


class PatientWithConstructor:

    def __init__(self, name, age):
        self.name = name
        self.age = age


patient1 = PatientWithConstructor("John", 42)
patient2 = PatientWithConstructor("Mary", 35)

print("\n========== PART 5: __init__ ==========")
print(patient1.name, patient1.age)
print(patient2.name, patient2.age)


# ============================================================
# PART 6 - self
# ============================================================

# self refers to the CURRENT OBJECT.
#
# If we write:
#
# patient1.introduce()
#
# self refers to patient1.
#
# If we write:
#
# patient2.introduce()
#
# self refers to patient2.
#
#
# Golden Rule:
#
# self = the current object
#
#
# Example:


class PatientWithMethod:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"My age is {self.age}.")


patient1 = PatientWithMethod("John", 42)
patient2 = PatientWithMethod("Mary", 35)

print("\n========== PART 6: self ==========")

patient1.introduce()
patient2.introduce()


# When patient1.introduce() runs:
#
# self -> patient1
#
# When patient2.introduce() runs:
#
# self -> patient2


# ============================================================
# PART 7 - INSTANCE VARIABLES
# ============================================================

# Instance variables belong to individual objects.
#
# They are usually created using self.
#
# Examples:
#
# self.name
# self.age
# self.weight
# self.height
#
#
# Each Patient can have different values.


class PatientInstance:

    def __init__(self, name, age, blood_group):
        self.name = name
        self.age = age
        self.blood_group = blood_group


patient1 = PatientInstance("John", 42, "A+")
patient2 = PatientInstance("Mary", 35, "O-")

print("\n========== PART 7: INSTANCE VARIABLES ==========")

print(patient1.name, patient1.age, patient1.blood_group)
print(patient2.name, patient2.age, patient2.blood_group)


# ============================================================
# PART 8 - CREATING MULTIPLE OBJECTS
# ============================================================

# One class can create many objects.
#
# Example:
#
# Patient class
#       |
#       +---- patient1
#       +---- patient2
#       +---- patient3
#
#
# Each object has its own instance data.


patient3 = PatientInstance("Peter", 67, "B+")

print("\n========== PART 8: MULTIPLE OBJECTS ==========")

print(patient1.name)
print(patient2.name)
print(patient3.name)


# ============================================================
# PART 9 - UPDATING OBJECT ATTRIBUTES
# ============================================================

# Object attributes can be changed after the object is created.
#
# Example:
#
# patient1.age = 43
#
# This changes patient1 only.


patient1.age = 43

print("\n========== PART 9: UPDATING ATTRIBUTES ==========")

print("John's updated age:", patient1.age)
print("Mary's age:", patient2.age)


# Changing patient1 does not change patient2.


# ============================================================
# PART 10 - CLASS VARIABLES VS INSTANCE VARIABLES
# ============================================================

# INSTANCE VARIABLE:
#
# Belongs to a specific object.
#
# Example:
#
# self.name
# self.age
#
#
# CLASS VARIABLE:
#
# Belongs to the class and can be shared by objects.
#
# Example:
#
# hospital = "Project Phoenix General Hospital"


class HospitalPatient:

    hospital = "Project Phoenix General Hospital"
    country = "Kenya"

    def __init__(self, name, age):
        self.name = name
        self.age = age


patient1 = HospitalPatient("John", 43)
patient2 = HospitalPatient("Mary", 35)

print("\n========== PART 10: CLASS VS INSTANCE ==========")

print(patient1.name)
print(patient1.hospital)

print(patient2.name)
print(patient2.hospital)


# Instance variables:
#
# patient1.name
# patient1.age
#
# Class variables:
#
# hospital
# country
#
#
# SENIOR ENGINEER NOTE:
# Ask:
#
# "Does this information belong to one object,
#  or does it describe the class as a whole?"
#
# This helps determine whether something should be an
# instance variable or a class variable.
#
# In a larger hospital system, however, we may eventually
# model Hospital as its own class instead of using a simple
# class variable.


# ============================================================
# PART 11 - METHODS
# ============================================================

# A method is a function that belongs to a class/object.
#
# Methods represent BEHAVIOUR.
#
# Healthcare examples:
#
# calculate_bmi()
# update_weight()
# introduce()
# add_diagnosis()
# book_appointment()
#
#
# Methods allow objects to DO things.


class PatientMethods:

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return bmi


patient1 = PatientMethods("John", 42, 72, 1.75)

print("\n========== PART 11: METHODS ==========")

print("BMI:", patient1.calculate_bmi())


# ============================================================
# PART 12 - HEALTHCARE BMI EXAMPLE
# ============================================================

# Healthcare systems must be careful with units.
#
# BMI uses:
#
# weight in kilograms
# height in metres
#
# But height may be recorded in centimetres.
#
# Example:
#
# 175 cm = 1.75 m
#
# Therefore we must convert:
#
# height_m = height / 100
#
#
# This was an important debugging lesson:
#
# Python does exactly what we tell it to do.
#
# If we give Python 175 and tell it that it is metres,
# Python will calculate using 175 metres.
#
# It does not know that we meant centimetres.


# ============================================================
# PART 13 - FINAL PATIENT CLASS
# ============================================================

class Patient:

    # --------------------------------------------------------
    # CLASS VARIABLES
    # --------------------------------------------------------

    hospital = "Project Phoenix General Hospital"
    country = "Kenya"

    # --------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------

    def __init__(self, name, age, blood_group, weight, height):
        self.name = name
        self.age = age
        self.blood_group = blood_group
        self.weight = weight
        self.height = height

    # --------------------------------------------------------
    # METHOD: INTRODUCE
    # --------------------------------------------------------

    def introduce(self):
        print(
            f"Hello, {self.name} is {self.age} years old "
            f"and has blood group {self.blood_group}."
        )

    # --------------------------------------------------------
    # METHOD: __str__
    # --------------------------------------------------------

    def __str__(self):
        return (
            f"Patient: {self.name} | "
            f"Age: {self.age} | "
            f"Blood Group: {self.blood_group}"
        )

    # --------------------------------------------------------
    # METHOD: CALCULATE BMI
    # --------------------------------------------------------

    def calculate_bmi(self):

        # Convert height from centimetres to metres.
        height_m = self.height / 100

        # Calculate BMI.
        bmi = self.weight / (height_m ** 2)

        # Return a clean result.
        return round(bmi, 2)

    # --------------------------------------------------------
    # METHOD: BMI CATEGORY
    # --------------------------------------------------------

    def bmi_category(self):

        # Reuse calculate_bmi() instead of duplicating
        # the BMI calculation.
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"

        elif bmi < 25:
            return "Normal weight"

        elif bmi < 30:
            return "Overweight"

        else:
            return "Obesity"

    # --------------------------------------------------------
    # METHOD: UPDATE WEIGHT
    # --------------------------------------------------------

    def update_weight(self, new_weight):

        # Basic validation.
        if new_weight <= 0:
            print("Weight must be greater than zero.")

        else:
            self.weight = new_weight


# ============================================================
# PART 14 - CREATING PATIENT OBJECTS
# ============================================================

patient1 = Patient(
    "John",
    42,
    "A+",
    70,
    175
)

patient2 = Patient(
    "Mary",
    35,
    "O-",
    60,
    160
)


# ============================================================
# PART 15 - UPDATING OBJECT DATA
# ============================================================

# Update John's age.

patient1.age = 43

# Update Mary's blood group.

patient2.blood_group = "O+"

# Update John's weight using the controlled method.

patient1.update_weight(75)


# ============================================================
# PART 16 - DISPLAY PATIENT 1
# ============================================================

print("\n========== PATIENT 1 ==========")

print("Name:", patient1.name)
print("Age:", patient1.age)
print("Blood Group:", patient1.blood_group)
print("Weight:", patient1.weight, "kg")
print("Height:", patient1.height, "cm")

print(
    f"{patient1.name}'s BMI: "
    f"{patient1.calculate_bmi()}"
)

print(
    f"{patient1.name}'s BMI category: "
    f"{patient1.bmi_category()}"
)

patient1.introduce()


# ============================================================
# PART 17 - DISPLAY PATIENT 2
# ============================================================

print("\n========== PATIENT 2 ==========")

print("Name:", patient2.name)
print("Age:", patient2.age)
print("Blood Group:", patient2.blood_group)
print("Weight:", patient2.weight, "kg")
print("Height:", patient2.height, "cm")

print(
    f"{patient2.name}'s BMI: "
    f"{patient2.calculate_bmi()}"
)

print(
    f"{patient2.name}'s BMI category: "
    f"{patient2.bmi_category()}"
)

patient2.introduce()


# ============================================================
# PART 18 - __str__() DEMONSTRATION
# ============================================================

# Python automatically uses __str__() when we print an object.

print("\n========== __str__() DEMONSTRATION ==========")

print(patient1)
print(patient2)


# Without __str__(), Python would normally display something
# similar to:
#
# <__main__.Patient object at 0x...>
#
# __str__() allows us to define a useful human-readable
# representation of the object.


# ============================================================
# PART 19 - VALIDATION TEST
# ============================================================

print("\n========== VALIDATION TEST ==========")

# Valid update.

patient1.update_weight(78)

print(
    f"{patient1.name}'s new weight: "
    f"{patient1.weight} kg"
)

# Invalid update.

patient1.update_weight(-10)

# The invalid value is rejected and the patient's weight
# remains unchanged.


# ============================================================
# PART 20 - FINAL OBJECT STATE
# ============================================================

print("\n========== FINAL PATIENT STATE ==========")

print(patient1)

print(
    f"BMI: {patient1.calculate_bmi()}"
)

print(
    f"BMI Category: {patient1.bmi_category()}"
)


# ============================================================
# PART 21 - DEBUGGING LESSONS
# ============================================================

# LESSON 1:
#
# Python does exactly what we tell it to do.
#
# If height is stored as centimetres:
#
# 175
#
# We must convert it to:
#
# 1.75
#
# before using the BMI formula.
#
#
# LESSON 2:
#
# self refers to the current object.
#
# patient1.introduce()
#     -> self = patient1
#
# patient2.introduce()
#     -> self = patient2
#
#
# LESSON 3:
#
# Instance variables belong to individual objects.
#
# patient1.age
# patient2.age
#
# They can contain different values.
#
#
# LESSON 4:
#
# Methods can reuse other methods.
#
# bmi_category() calls:
#
# self.calculate_bmi()
#
# This avoids duplicating logic.


# ============================================================
# PART 22 - BASIC ENCAPSULATION
# ============================================================

# Encapsulation means keeping related data and behaviour
# together and controlling how data is accessed or changed.
#
# Python commonly uses a single underscore as a convention:
#
# self._weight
#
# This communicates:
#
# "This attribute is intended for internal use."
#
# It does NOT make the attribute completely inaccessible.
#
# Example:
#
# class Patient:
#
#     def __init__(self, weight):
#         self._weight = weight
#
#
# Python developers generally treat _weight as an internal
# implementation detail.
#
#
# Healthcare connection:
#
# Sensitive clinical information should not be changed
# casually by unrelated parts of a large application.
#
# Controlled methods can provide:
#
# validation
# auditing
# permissions
# safety checks
#
# These concepts become increasingly important in healthcare
# software.


# ============================================================
# PART 23 - CLEAN CLASS DESIGN PRINCIPLES
# ============================================================

# 1. Give a class ONE clear responsibility.
#
# Patient -> represents a patient.
#
# Later:
#
# Doctor
# Appointment
# Prescription
# Medication
# LaboratoryTest
# Invoice
#
# should be separate classes.
#
#
# 2. Use meaningful names.
#
# Good:
#
# blood_group
# calculate_bmi()
# update_weight()
#
#
# 3. Avoid unnecessary duplication.
#
# Good:
#
# bmi = self.calculate_bmi()
#
# instead of repeating the BMI formula.
#
#
# 4. Validate important data.
#
# Example:
#
# weight must be greater than zero.
#
#
# 5. Keep methods focused.
#
# calculate_bmi() -> calculates BMI.
#
# bmi_category() -> determines category.
#
# update_weight() -> validates and updates weight.
#
#
# 6. Don't add complexity unnecessarily.
#
# A simple class is often better than an over-engineered one.
#
#
# 7. Think about data representation.
#
# Healthcare software must be explicit about units:
#
# kg
# g
# cm
# m
# mL
# L
# mmHg
# kPa
#
# Unit mistakes can produce clinically dangerous results.


# ============================================================
# PART 24 - SENIOR ENGINEER NOTES
# ============================================================

# Senior Engineer Principle 1:
#
# OOP is not just about writing classes.
# It is about designing meaningful software models.
#
#
# Senior Engineer Principle 2:
#
# Data and behaviour that naturally belong together
# should usually be kept together.
#
#
# Senior Engineer Principle 3:
#
# Avoid duplicated logic.
#
# If one method already performs a calculation, reuse it.
#
#
# Senior Engineer Principle 4:
#
# Validation should happen as close as practical to the
# point where data enters or changes the system.
#
#
# Senior Engineer Principle 5:
#
# Good software models real-world relationships clearly.
#
# Patient
#     |
#     +---- Appointment
#                 |
#                 +---- Doctor
#
#
# Senior Engineer Principle 6:
#
# Simplicity is a feature.
# Do not add abstraction simply to appear advanced.


# ============================================================
# PART 25 - HEALTHCARE AI CONNECTION
# ============================================================

# OOP provides a foundation for building structured
# healthcare software.
#
# A Patient object might eventually contain:
#
# demographic information
# clinical information
# medications
# laboratory results
# vital signs
# diagnoses
# appointments
#
#
# These structured objects could eventually feed into:
#
# databases
# APIs
# machine learning pipelines
# LLM applications
# clinical decision-support systems
#
#
# Conceptual architecture:
#
#
# Patient Object
#       |
#       v
# Structured Clinical Data
#       |
#       v
# Data Validation
#       |
#       v
# Feature Preparation
#       |
#       v
# AI / ML Model
#       |
#       v
# Risk Prediction
#       |
#       v
# Clinical Decision Support
#
#
# IMPORTANT:
#
# AI systems in healthcare must be designed with validation,
# privacy, security, auditability, and clinical safety in mind.


# ============================================================
# PART 26 - MINI PROJECT: PATIENT MANAGEMENT OBJECT
# ============================================================

# Project goal:
#
# Create a Patient object that can:
#
# 1. Store patient information.
# 2. Display patient information.
# 3. Calculate BMI.
# 4. Determine BMI category.
# 5. Update weight safely.
#
#
# Example:
#
# patient = Patient(
#     "Alice",
#     30,
#     "B+",
#     65,
#     168
# )
#
# patient.update_weight(67)
#
# print(patient)
# print(patient.calculate_bmi())
# print(patient.bmi_category())
#
#
# Expected structure:
#
# Patient
#   |
#   +-- Attributes
#   |      name
#   |      age
#   |      blood_group
#   |      weight
#   |      height
#   |
#   +-- Methods
#          introduce()
#          __str__()
#          calculate_bmi()
#          bmi_category()
#          update_weight()


# ============================================================
# PART 27 - LESSON 18 CHALLENGES
# ============================================================

# CHALLENGE 1:
#
# Create a Doctor class with:
#
# name
# specialty
# license_number
#
# Add an introduce() method.
#
#
# CHALLENGE 2:
#
# Create an Appointment class with:
#
# patient
# doctor
# date
# time
#
#
# CHALLENGE 3:
#
# Create a LaboratoryTest class with:
#
# test_name
# result
# status
#
#
# CHALLENGE 4:
#
# Add validation so that a patient's age cannot be negative.
#
#
# CHALLENGE 5:
#
# Add a method to Patient called:
#
# update_height()
#
# Validate that height is greater than zero.
#
#
# CHALLENGE 6:
#
# Think about how Patient and Appointment objects could
# interact with each other.
#
#
# Example:
#
# appointment = Appointment(patient1, doctor1, ...)
#
#
# This will become important in the Hospital Management
# System we build in future Project Phoenix lessons.


# ============================================================
# PART 28 - KEY TAKEAWAYS
# ============================================================

# 1. OOP organizes software around objects.
#
# 2. A class is a blueprint.
#
# 3. An object is an actual instance of a class.
#
# 4. Attributes store object data.
#
# 5. Methods define object behaviour.
#
# 6. __init__ initializes a new object.
#
# 7. self refers to the current object.
#
# 8. Instance variables belong to individual objects.
#
# 9. Class variables can be shared across objects.
#
# 10. Multiple objects can be created from one class.
#
# 11. Object attributes can be updated.
#
# 12. __str__() provides a useful human-readable
#     representation of an object.
#
# 13. A leading underscore is a Python convention for
#     indicating internal attributes.
#
# 14. Methods can validate and control changes to data.
#
# 15. Good classes have clear responsibilities.
#
# 16. Avoid unnecessary duplication.
#
# 17. Healthcare software requires careful handling of
#     units, validation, privacy, and safety.
#
# 18. OOP provides the foundation for modelling complex
#     healthcare systems.


# ============================================================
# PROJECT PHOENIX - LESSON 18 COMPLETE
# ============================================================
#
# NEXT DIRECTION:
#
# Build additional healthcare classes and gradually connect
# them into a Hospital Management System.
#
# Planned domain objects may include:
#
# Patient
# Doctor
# Appointment
# Prescription
# Medication
# LaboratoryTest
# Invoice
# Hospital
#
# The long-term goal is to move from isolated Python
# exercises toward real software architecture suitable for
# Healthcare AI engineering.
#
# ============================================================