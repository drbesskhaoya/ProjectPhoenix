# ============================================================
# PROJECT PHOENIX — LESSON 22
# ============================================================
# Topic: Abstraction in Object-Oriented Programming
# Week 2 — Object-Oriented Programming
#
# Lesson Objective:
# Understand abstraction and learn how abstract classes
# create a common contract for healthcare systems and AI
# services.
# ============================================================


# ============================================================
# 1. WHAT IS ABSTRACTION?
# ============================================================
#
# Abstraction means defining WHAT an object must do without
# exposing all the details of HOW it does it.
#
# Healthcare example:
#
# When using an ECG machine, a doctor may simply:
#
#     Start ECG -> Record ECG -> View result
#
# The doctor does not need to know how the machine:
#
# - detects electrical signals
# - processes the signals
# - filters noise
# - generates the waveform
#
# The complex implementation is hidden.
#
# KEY IDEA:
#
# Abstraction defines WHAT must be done.
# The subclass defines HOW it is done.
#


# ============================================================
# 2. ABSTRACT CLASSES
# ============================================================
#
# Python provides ABC and abstractmethod through the abc module.
#
# ABC = Abstract Base Class
#
# abstractmethod marks a method that subclasses must implement.
#

from abc import ABC, abstractmethod


# ============================================================
# 3. BASIC ABSTRACT CLASS
# ============================================================

class MedicalDevice(ABC):

    @abstractmethod
    def run_test(self):
        pass


# MedicalDevice defines a requirement:
#
# Every concrete medical device must provide run_test().
#
# The parent class does not provide the actual implementation.
#


# ============================================================
# 4. ABSTRACT PARENT AND CONCRETE CHILD
# ============================================================
#
# Think of the structure like this:
#
#                 MedicalDevice
#                       |
#          +------------+------------+
#          |                         |
#      ECGMachine             XRayMachine
#
# MedicalDevice establishes the requirement.
# Each child provides its own implementation.
#


class ECGMachine(MedicalDevice):

    def run_test(self):
        print("Running ECG test...")


class BloodPressureMonitor(MedicalDevice):

    def run_test(self):
        print("Measuring blood pressure...")


# Both classes have run_test(), but each performs a different
# operation.
#


# ============================================================
# 5. ABSTRACT CLASSES CANNOT BE INSTANTIATED DIRECTLY
# ============================================================
#
# This would produce an error:
#
# device = MedicalDevice()
#
# Why?
#
# MedicalDevice is incomplete.
#
# It says:
#
# "A medical device must be able to run a test."
#
# But it does not define the actual test.
#
# A concrete subclass must provide that implementation.
#


# ============================================================
# 6. HEALTHCARE EXAMPLE — X-RAY MACHINE
# ============================================================

class XRayMachine(MedicalDevice):

    def __init__(self, model, manufacturer):
        self.model = model
        self.manufacturer = manufacturer

    def run_test(self):
        print(f"Running test with {self.model} by {self.manufacturer}.")

    def stop_test(self):
        print(f"Stopping test with {self.model}.")


xray = XRayMachine("XR-500", "Phoenix Medical")

xray.run_test()


# Expected output:
#
# Running test with XR-500 by Phoenix Medical.


# ============================================================
# 7. ABSTRACTION IN HEALTHCARE AI
# ============================================================
#
# Project Phoenix can use the same idea for AI services.
#
# Possible architecture:
#
#                    AIService
#                        |
#             +----------+----------+
#             |                     |
#         TriageAI          RiskPredictionAI
#
# AIService can define a common requirement:
#
# Every AI service must provide predict().
#


class AIService(ABC):

    @abstractmethod
    def predict(self, data):
        pass


# ============================================================
# 8. TRIAGE AI
# ============================================================

class TriageAI(AIService):

    def predict(self, data):
        print(f"Running patient triage prediction...: {data}")
        return "Triage Prediction Result"


triage = TriageAI()

triage.predict("patient data")


# Expected output:
#
# Running patient triage prediction...: patient data


# ============================================================
# 9. RISK PREDICTION AI
# ============================================================

class RiskPredictionAI(AIService):

    def predict(self, data):
        print(f"Running risk prediction...: {data}")
        return "Risk Prediction Result"


risk = RiskPredictionAI()

risk.predict("patient data")


# Expected output:
#
# Running risk prediction...: patient data


# ============================================================
# 10. ABSTRACTION + POLYMORPHISM
# ============================================================
#
# This connects Lesson 22 to Lesson 21.
#
# Abstraction defines the common contract:
#
#     AIService
#         |
#         +--> must provide predict()
#
# Polymorphism allows different AI services to implement
# predict() differently.
#

services = [
    TriageAI(),
    RiskPredictionAI()
]

for service in services:
    service.predict("patient data")


# The same method call:
#
#     service.predict()
#
# can produce different behaviour depending on the object.
#
# This is polymorphism operating through an abstract interface.


# ============================================================
# 11. DEBUGGING EXAMPLE
# ============================================================
#
# Consider:
#
# class AIService(ABC):
#
#     @abstractmethod
#     def predict(self, data):
#         pass
#
#
# class TriageAI(AIService):
#     pass
#
#
# triage = TriageAI()
#
#
# This fails because TriageAI has not implemented predict().
#
# The fix is:
#
# class TriageAI(AIService):
#
#     def predict(self, data):
#         print("Running patient triage prediction...")
#
#
# Once the abstract method is implemented, the class can
# be instantiated.
#


# ============================================================
# 12. COMMON MISTAKES
# ============================================================
#
# MISTAKE 1:
# Forgetting to inherit from the abstract class.
#
# Incorrect:
#
# class XRayMachine:
#
# Correct:
#
# class XRayMachine(MedicalDevice):
#
#
# MISTAKE 2:
# Forgetting to implement the abstract method.
#
# If the parent requires:
#
#     run_test()
#
# the child must implement run_test().
#
#
# MISTAKE 3:
# Incorrect indentation.
#
# Methods must be inside the class:
#
# class XRayMachine(MedicalDevice):
#
#     def run_test(self):
#         print("Running X-ray scan...")
#
#
# MISTAKE 4:
# Trying to instantiate an incomplete subclass.
#
# class TriageAI(AIService):
#     pass
#
# triage = TriageAI()
#
# This fails because predict() has not been implemented.
#


# ============================================================
# 13. HEALTHCARE AI CONNECTION
# ============================================================
#
# Abstraction gives Project Phoenix a consistent architecture.
#
# Future Phoenix AI services could include:
#
#     TriageAI
#     RiskPredictionAI
#     ClinicalDecisionSupportAI
#     DrugInteractionAI
#     PatientReadmissionAI
#
# Different services can have completely different internal
# logic while following the same basic interface.
#
# This makes systems easier to:
#
# - extend
# - test
# - maintain
# - replace
# - integrate
#
# IMPORTANT:
#
# A real clinical AI system would also require validation,
# safety controls, monitoring, governance, and human oversight.
# The examples here demonstrate software architecture only.
#


# ============================================================
# 14. SENIOR ENGINEER NOTES
# ============================================================
#
# 1. Abstraction is about CONTRACTS.
#
# Ask:
#
#     "What must this class be able to do?"
#
# rather than immediately asking:
#
#     "How will it do it?"
#
#
# 2. Do not use abstraction unnecessarily.
#
# Use it when multiple related classes need to follow a common
# structure or contract.
#
#
# 3. Abstraction and polymorphism often work together.
#
# A common architecture is:
#
#     Abstraction
#          |
#     Common contract
#          |
#     Inheritance
#          |
#     Different implementations
#          |
#     Polymorphism
#
#
# 4. Good architecture hides unnecessary complexity.
#
# A user of an AI service should not need to understand every
# internal detail of the model.
#
# They should be able to interact with a clear interface.
#
# Example:
#
#     prediction = triage.predict(patient_data)
#
# The internal implementation can be much more complex.
#


# ============================================================
# 15. LESSON 22 MINI-PROJECT
# ============================================================
#
# Build an abstract AIService and two concrete AI services.
#
# The completed example is:
#

class PhoenixAIService(ABC):

    @abstractmethod
    def predict(self, data):
        pass


class PhoenixTriageAI(PhoenixAIService):

    def predict(self, data):
        print(f"Running Phoenix triage prediction...: {data}")
        return "Triage Prediction Result"


class PhoenixRiskAI(PhoenixAIService):

    def predict(self, data):
        print(f"Running Phoenix risk prediction...: {data}")
        return "Risk Prediction Result"


phoenix_triage = PhoenixTriageAI()
phoenix_risk = PhoenixRiskAI()

phoenix_triage.predict("patient data")
phoenix_risk.predict("patient data")


# ============================================================
# 16. KEY TAKEAWAYS
# ============================================================
#
# 1. Abstraction hides implementation details.
#
# 2. ABC is used to create abstract base classes.
#
# 3. @abstractmethod defines a method that subclasses must
#    implement.
#
# 4. Abstract classes cannot normally be instantiated directly.
#
# 5. Subclasses provide the concrete implementation.
#
# 6. Abstraction establishes a CONTRACT.
#
# 7. Different subclasses can implement the same contract
#    differently.
#
# 8. Abstraction and polymorphism work particularly well
#    together.
#
# 9. Healthcare systems can use abstraction to create
#    consistent AI-service architectures.
#
# 10. Good software architecture focuses on clear interfaces
#     and responsibilities.
#


# ============================================================
# 17. PROJECT PHOENIX PRINCIPLE
# ============================================================
#
#     DEFINE THE CONTRACT FIRST.
#     LET EACH COMPONENT DECIDE HOW TO FULFIL IT.
#
#
# In Phoenix:
#
#     AIService
#          |
#          v
#     Defines what an AI service must provide
#          |
#          v
#     TriageAI / RiskPredictionAI
#          |
#          v
#     Provide their own implementations
#
#
# ============================================================
# LESSON 22 COMPLETE
# ============================================================
#
# Topic:
#     Abstraction
#
# Core tools:
#     ABC
#     @abstractmethod
#
# Healthcare applications:
#     MedicalDevice
#     AIService
#
# OOP connection:
#     Abstraction + Inheritance + Polymorphism
#
# Project Phoenix Progress:
#     Lessons 1–22 COMPLETE
#
# ============================================================