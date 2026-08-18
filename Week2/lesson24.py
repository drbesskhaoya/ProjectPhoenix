==========================================================
# PROJECT PHOENIX - LESSON 24 HANDBOOK
# Composition and Abstraction
# ============================================================

# LESSON GOALS
# 1. Understand composition.
# 2. Understand abstraction.
# 3. Understand IS-A vs HAS-A.
# 4. See how these ideas apply to Phoenix.


# ============================================================
# 1. COMPOSITION
# ============================================================
# Composition means:
# One class HAS another class.
#
# Example:
# A HospitalSystem HAS a PatientManager.


class PatientManager:
    def register_patient(self):
        print("Patient registered")


class HospitalSystem:
    def __init__(self):
        self.patient_manager = PatientManager()

    def register(self):
        self.patient_manager.register_patient()


hospital = HospitalSystem()
hospital.register()


# Expected output:
# Patient registered


# ============================================================
# 2. INHERITANCE VS COMPOSITION
# ============================================================
#
# INHERITANCE = IS-A
#
# A Patient IS A Person.
#
# COMPOSITION = HAS-A
#
# A HospitalSystem HAS A PatientManager.


class Person:
    pass


class Patient(Person):
    pass


class Hospital:
    def __init__(self):
        self.patient_manager = PatientManager()


# Memory trick:
#
# IS-A  -> Inheritance
# HAS-A -> Composition


# ============================================================
# 3. ABSTRACTION
# ============================================================
# Abstraction means:
# Hide complicated internal work and expose only what
# the user needs.
#
# Example:
# A doctor can request a risk assessment without needing
# to know every calculation performed by the AI.


class RiskPredictionAI:
    def predict(self, patient):
        print("Running risk prediction...")
        return "High risk"


risk_ai = RiskPredictionAI()

result = risk_ai.predict("Patient 001")

print(result)


# ============================================================
# 4. PHOENIX EXAMPLE
# ============================================================
# The HospitalSystem uses the RiskPredictionAI.
# This is composition.


class PhoenixHospitalSystem:
    def __init__(self):
        self.risk_ai = RiskPredictionAI()

    def assess_risk(self, patient):
        result = self.risk_ai.predict(patient)
        print(f"Result: {result}")


phoenix = PhoenixHospitalSystem()
phoenix.assess_risk("Patient 001")


# Expected output:
#
# Running risk prediction...
# Result: High risk


# ============================================================
# 5. PRACTICE
# ============================================================
#
# Question 1:
# A HospitalSystem contains a PatientManager.
#
# Answer:
# Composition
#
# Question 2:
# A doctor uses risk_ai.predict(patient) without knowing
# how the AI calculates the risk.
#
# Answer:
# Abstraction


# ============================================================
# 6. MINI PROJECT
# ============================================================
# Build a simple healthcare system containing:
#
# - PatientManager
# - RiskPredictionAI
# - HospitalSystem
#
# The HospitalSystem should use both components.


class PhoenixPatientManager:
    def register_patient(self, patient):
        print(f"Patient registered: {patient}")


class PhoenixRiskAI:
    def predict(self, patient):
        print(f"Running risk prediction for {patient}...")
        return "High risk"


class PhoenixSystem:
    def __init__(self):
        self.patient_manager = PhoenixPatientManager()
        self.risk_ai = PhoenixRiskAI()

    def register_patient(self, patient):
        self.patient_manager.register_patient(patient)

    def assess_risk(self, patient):
        result = self.risk_ai.predict(patient)
        print(f"Risk result: {result}")


system = PhoenixSystem()

system.register_patient("Patient 001")
system.assess_risk("Patient 001")


# ============================================================
# 7. KEY TAKEAWAYS
# ============================================================
#
# COMPOSITION:
# One class HAS another class.
#
# Example:
# self.patient_manager = PatientManager()
#
# INHERITANCE:
# One class IS another type of class.
#
# Example:
# class Patient(Person):
#
# ABSTRACTION:
# Hide complicated internal work and expose a simple interface.
#
# Example:
# risk_ai.predict(patient)
#
#
# EASY MEMORY TRICK:
#
# IS-A  -> Inheritance
# HAS-A -> Composition
# HIDE COMPLEXITY -> Abstraction
#
#
# PROJECT PHOENIX STATUS:
# Lesson 24 complete.
#
# Concepts covered:
# - Encapsulation
# - Inheritance
# - Polymorphism
# - Composition
# - Abstraction
#