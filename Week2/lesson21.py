# ============================================================
# PROJECT PHOENIX — LESSON 21
# POLYMORPHISM
# ============================================================

# WEEK 2 — OBJECT-ORIENTED PROGRAMMING
#
# Goal:
# Understand how different objects can respond to the same
# method in different ways.
#
# Healthcare AI Connection:
# Polymorphism allows Phoenix to work with different healthcare
# professionals and system components through common behaviours.


# ============================================================
# 1. WHAT IS POLYMORPHISM?
# ============================================================

# Polymorphism means "many forms".
#
# Different classes can have the same method name but
# different implementations.


class Doctor:
    def work(self):
        print("Doctor is diagnosing patients.")


class Nurse:
    def work(self):
        print("Nurse is monitoring patients.")


doctor = Doctor()
nurse = Nurse()

doctor.work()
nurse.work()

# Output:
# Doctor is diagnosing patients.
# Nurse is monitoring patients.


# ============================================================
# 2. METHOD OVERRIDING
# ============================================================

# A child class can provide its own version of a method
# inherited from a parent class.


class Person:
    def work(self):
        print("Person is working.")


class Doctor(Person):
    def work(self):
        print("Doctor is diagnosing patients.")


doctor = Doctor()
doctor.work()

# Output:
# Doctor is diagnosing patients.


# ============================================================
# 3. POLYMORPHISM WITH INHERITANCE
# ============================================================

class Person:
    def work(self):
        print("Person is working.")


class Doctor(Person):
    def work(self):
        print("Doctor is diagnosing patients.")


class Nurse(Person):
    def work(self):
        print("Nurse is monitoring patients.")


people = [Doctor(), Nurse()]

for person in people:
    person.work()

# Output:
# Doctor is diagnosing patients.
# Nurse is monitoring patients.


# ============================================================
# 4. WHY POLYMORPHISM IS USEFUL
# ============================================================

# We do NOT need to write:
#
# if person is a Doctor:
#     ...
# elif person is a Nurse:
#     ...
#
# Instead, we can simply call the common method.


for person in people:
    person.work()


# ============================================================
# 5. INHERITED BEHAVIOUR
# ============================================================

# A child class does not have to override every method.
# If it doesn't, Python uses the parent's method.


class Person:
    def introduce(self):
        print("I am a person.")


class Doctor(Person):
    def introduce(self):
        print("I am a doctor.")


class Patient(Person):
    pass


people = [Doctor(), Patient()]

for person in people:
    person.introduce()

# Output:
# I am a doctor.
# I am a person.


# ============================================================
# 6. DUCK TYPING
# ============================================================

# Python often cares about what an object CAN DO,
# rather than what class it belongs to.
#
# "If it behaves like the thing we need, we can use it."


class Doctor:
    def work(self):
        print("Doctor is working.")


class AIModel:
    def work(self):
        print("AI is analyzing patient data.")


workers = [Doctor(), AIModel()]

for worker in workers:
    worker.work()

# Output:
# Doctor is working.
# AI is analyzing patient data.


# ============================================================
# 7. HEALTHCARE PROFESSIONALS
# ============================================================

# Phoenix can use a common parent class for healthcare
# professionals.


class HealthcareProfessional:
    def work(self):
        print("Healthcare professional is working.")


class Doctor(HealthcareProfessional):
    def work(self):
        print("Doctor is diagnosing patients.")


class Nurse(HealthcareProfessional):
    def work(self):
        print("Nurse is monitoring patients.")


class Radiologist(HealthcareProfessional):
    def work(self):
        print("Radiologist is analyzing medical images.")


class Pharmacist(HealthcareProfessional):
    def work(self):
        print("Pharmacist is dispensing medications.")


staff = [
    Doctor(),
    Nurse(),
    Radiologist(),
    Pharmacist()
]

for member in staff:
    member.work()

# Output:
# Doctor is diagnosing patients.
# Nurse is monitoring patients.
# Radiologist is analyzing medical images.
# Pharmacist is dispensing medications.


# ============================================================
# 8. PROJECT PHOENIX ARCHITECTURE
# ============================================================

# Current architecture:
#
# Person
# ├── Patient
# ├── Doctor
# └── Nurse
#
# Inheritance:
# "Doctor IS A Person"
# "Nurse IS A Person"
# "Patient IS A Person"
#
# Polymorphism:
# Each class can provide its own implementation of a method.


class Person:
    def describe_role(self):
        print("I am a person.")


class Doctor(Person):
    def describe_role(self):
        print("Doctor provides medical diagnosis.")


class Nurse(Person):
    def describe_role(self):
        print("Nurse provides patient care.")


class Patient(Person):
    def describe_role(self):
        print("Patient receives healthcare.")


people = [
    Doctor(),
    Nurse(),
    Patient()
]

for person in people:
    person.describe_role()


# ============================================================
# 9. MINI PROJECT — PHOENIX HEALTHCARE STAFF
# ============================================================

class HealthcareProfessional:
    def work(self):
        print("Healthcare professional is working.")


class Doctor(HealthcareProfessional):
    def work(self):
        print("Doctor is diagnosing patients.")


class Nurse(HealthcareProfessional):
    def work(self):
        print("Nurse is monitoring patients.")


class Radiologist(HealthcareProfessional):
    def work(self):
        print("Radiologist is analyzing medical images.")


class Pharmacist(HealthcareProfessional):
    def work(self):
        print("Pharmacist is dispensing medications.")


staff = [
    Doctor(),
    Nurse(),
    Radiologist(),
    Pharmacist()
]

for member in staff:
    member.work()


# ============================================================
# 10. DEBUGGING EXERCISE
# ============================================================

# What will this print?


class Person:
    def work(self):
        print("Person is working.")


class Doctor(Person):
    def diagnose(self):
        print("Doctor is diagnosing patients.")


people = [Doctor()]

for person in people:
    person.work()

# Output:
# Person is working.
#
# Why?
# Doctor did NOT override work().
# Doctor created a different method called diagnose().
# Therefore Doctor inherits Person's work().


# ============================================================
# 11. COMMON MISTAKES
# ============================================================

# Mistake 1:
# Confusing inheritance with polymorphism.
#
# Inheritance:
# "What does this class inherit?"
#
# Polymorphism:
# "How can different objects respond to the same operation?"


# Mistake 2:
# Checking every class manually when a common method exists.
#
# Avoid unnecessary code such as:
#
# if isinstance(worker, Doctor):
#     ...
# elif isinstance(worker, Nurse):
#     ...
#
# Polymorphism can often remove this repetitive logic.


# Mistake 3:
# Poor class naming.
#
# Python convention:
#
# class Doctor:
# class Nurse:
# class HealthcareProfessional:
#
# Avoid:
#
# class doctor:
# class nurse:


# ============================================================
# 12. SENIOR ENGINEER NOTES
# ============================================================

# 1. Program around behaviour.
#
# Focus on what an object can DO rather than constantly
# checking what exact class it belongs to.


# 2. Polymorphism reduces conditional logic.
#
# Different objects can implement the same method differently.


# 3. Polymorphism improves extensibility.
#
# Phoenix can add new healthcare roles without necessarily
# rewriting existing code.
#
# Example:
#
# Doctor
# Nurse
# Radiologist
# Pharmacist
# Physiotherapist
# Dietitian


# 4. Use meaningful inheritance.
#
# Inheritance should represent a genuine IS-A relationship.
#
# Doctor IS A Person
# Nurse IS A Person
# Patient IS A Person


# ============================================================
# 13. HEALTHCARE AI CONNECTION
# ============================================================

# A future Phoenix system may contain:
#
# Doctor
# Nurse
# Patient
# AI Risk Model
# Laboratory System
# Radiology System
# Billing System
# Notification System
#
# These components may have different implementations but
# can expose common behaviours.
#
# Example:
#
# for component in components:
#     component.run()
#
# The risk model might calculate risk.
# The notification service might send an alert.
# The laboratory system might retrieve results.
#
# The calling code does not need to know every implementation
# detail.


# ============================================================
# 14. KEY TAKEAWAYS
# ============================================================

# Polymorphism = "many forms"
#
# Same method
#     ↓
# Different objects
#     ↓
# Different behaviour
#
# Remember:
#
# 1. Different objects can respond differently to the same method.
# 2. Method overriding is a common form of polymorphism.
# 3. Child classes can replace inherited behaviour.
# 4. Child classes can also inherit behaviour without overriding it.
# 5. Python supports duck typing.
# 6. Duck typing focuses on behaviour rather than exact class type.
# 7. Polymorphism reduces unnecessary conditional logic.
# 8. Polymorphism makes systems easier to extend.
# 9. Good naming and meaningful abstractions matter.
# 10. Phoenix will use polymorphism as its architecture becomes
#     more sophisticated.


# ============================================================
# PHOENIX PRINCIPLE
# ============================================================

# Build components around behaviour so Phoenix can work with
# different healthcare roles and system components without
# unnecessary hard-coded logic.


# ============================================================
# LESSON 21 COMPLETE
# ============================================================