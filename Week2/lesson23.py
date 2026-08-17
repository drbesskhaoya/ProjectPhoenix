# ============================================================
# PROJECT PHOENIX
# LESSON 23 - ABSTRACTION AND ABSTRACT CLASSES
# ============================================================

"""
LESSON GOAL
-----------
Understand abstraction and abstract classes in Python.

By the end of this lesson, you should understand:

1. What abstraction means.
2. What an abstract class is.
3. What ABC means.
4. What @abstractmethod does.
5. Why child classes must implement abstract methods.
6. How abstraction works together with polymorphism.
7. How this can be used in Project Phoenix.
"""


# ============================================================
# 1. WHAT IS ABSTRACTION?
# ============================================================

"""
Abstraction means hiding unnecessary implementation details
and exposing only what is important.

Healthcare example:

When a doctor uses an ECG machine, they do not need to know
how the machine processes every electrical signal internally.

They simply use the interface provided by the machine.

In software, abstraction works in a similar way.

We define WHAT something must do without necessarily defining
HOW it must do it.
"""


# ============================================================
# 2. ABSTRACT CLASSES
# ============================================================

"""
An abstract class is a blueprint or contract for other classes.

Python provides the ABC module for creating abstract classes.
"""

from abc import ABC, abstractmethod


class AIService(ABC):

    @abstractmethod
    def predict(self):
        pass


"""
AIService is an abstract class.

The predict() method is an abstract method.

The abstract class is telling every AI service:

    "You must provide a predict() method."

The parent class does not decide exactly how prediction works.

The child class decides that.
"""


# ============================================================
# 3. RISK PREDICTION AI
# ============================================================

class RiskPredictionAI(AIService):

    def predict(self):
        print("Running risk prediction...")


risk_ai = RiskPredictionAI()

risk_ai.predict()


# Expected output:
#
# Running risk prediction...


# ============================================================
# 4. DIAGNOSIS AI
# ============================================================

class DiagnosisAI(AIService):

    def predict(self):
        print("Running diagnosis AI...")


diagnosis_ai = DiagnosisAI()

diagnosis_ai.predict()


# Expected output:
#
# Running diagnosis AI...


# ============================================================
# 5. THE SAME CONTRACT
# ============================================================

"""
Both classes inherit from AIService.

Both classes must provide:

    predict()

However, they can implement predict() differently.

RiskPredictionAI:
    predicts patient risk.

DiagnosisAI:
    performs diagnosis-related AI processing.

This is the power of abstraction.
"""


# ============================================================
# 6. WHAT HAPPENS IF WE DO NOT IMPLEMENT predict()?
# ============================================================

"""
This class would be incomplete:

    class IncompleteAI(AIService):
        pass

Because AIService requires predict(), Python will not allow
us to create an IncompleteAI object.

This protects our system from incomplete AI services.

We do NOT run the incomplete example here because it would
intentionally produce an error.
"""


# ============================================================
# 7. ABSTRACTION AND POLYMORPHISM
# ============================================================

"""
Abstraction and polymorphism work very well together.

Abstraction establishes the common requirement:

    Every AI service must have predict().

Polymorphism allows different AI services to respond to
predict() in different ways.
"""


services = [
    RiskPredictionAI(),
    DiagnosisAI()
]

for service in services:
    service.predict()


# Expected output:
#
# Running risk prediction...
# Running diagnosis AI...


# ============================================================
# 8. PROJECT PHOENIX EXAMPLE
# ============================================================

"""
Imagine Project Phoenix eventually contains many AI services:

    AIService
        |
        |--- RiskPredictionAI
        |
        |--- DiagnosisAI
        |
        |--- PatientMonitoringAI
        |
        |--- ReadmissionPredictionAI
        |
        |--- MedicationRiskAI

Every service follows the same basic contract:

    predict()

Phoenix can therefore interact with different AI services
without needing to know every implementation detail.
"""


class PatientMonitoringAI(AIService):

    def predict(self):
        print("Monitoring patient status...")


patient_ai = PatientMonitoringAI()

patient_ai.predict()


# Expected output:
#
# Monitoring patient status...


# ============================================================
# 9. WHY THIS IS USEFUL IN PHOENIX
# ============================================================

"""
Without abstraction, different AI services could have
completely different interfaces.

For example:

    RiskPredictionAI -> calculate_risk()
    DiagnosisAI -> diagnose_patient()
    MonitoringAI -> monitor_patient()

That would make the system harder to manage.

With abstraction, we can establish a common interface:

    predict()

Every AI service follows the same basic contract.

This makes Phoenix easier to extend and maintain.
"""


# ============================================================
# 10. ABSTRACTION VS POLYMORPHISM
# ============================================================

"""
ABSTRACTION

Defines what must exist.

Example:

    Every AI service must have predict().


POLYMORPHISM

Allows the same method to behave differently depending
on the object.

Example:

    RiskPredictionAI.predict()

and

    DiagnosisAI.predict()

perform different tasks.


Simple memory rule:

    ABSTRACTION = WHAT

    POLYMORPHISM = DIFFERENT WAYS OF DOING IT
"""


# ============================================================
# 11. KEY TERMS
# ============================================================

"""
ABC
---
Abstract Base Class.

Used as the foundation for creating abstract classes.


@abstractmethod
----------------
Marks a method as required for child classes.


pass
----
Indicates that the abstract method has no implementation
in the parent class.


ABSTRACT CLASS
--------------
A blueprint or contract that defines requirements for
subclasses.
"""


# ============================================================
# 12. COMMON MISTAKE
# ============================================================

"""
Do not confuse inheritance with abstraction.

Inheritance can allow a child class to receive functionality
from a parent class.

Abstraction can require a child class to provide a specific
method.

Example:

    class AIService(ABC):

        @abstractmethod
        def predict(self):
            pass

The parent is not providing a working prediction system.

It is establishing a requirement.
"""


# ============================================================
# 13. CORE CONCEPT
# ============================================================

"""
The most important idea from Lesson 23:

    Abstraction defines WHAT a service must do.

    The subclass defines HOW it does it.


Project Phoenix example:

    AIService
        |
        +-- predict()
                |
                +-- RiskPredictionAI
                |
                +-- DiagnosisAI
                |
                +-- PatientMonitoringAI
"""


# ============================================================
# 14. LESSON 23 PRACTICE
# ============================================================

"""
Try creating another Phoenix AI service.

Challenge:

Create a class called:

    ReadmissionPredictionAI

It should inherit from:

    AIService

It must implement:

    predict()

And should print:

    Running readmission prediction...

The important part is not memorising the code.

The important part is understanding that the child class
must fulfil the contract established by AIService.
"""


# ============================================================
# 15. KEY TAKEAWAYS
# ============================================================

"""
1. Abstraction hides unnecessary implementation details.

2. An abstract class acts as a blueprint or contract.

3. ABC means Abstract Base Class.

4. @abstractmethod creates a required method.

5. A child class must implement an abstract method before
   its object can be created.

6. Different child classes can implement the same method
   differently.

7. Abstraction and polymorphism work together.

8. Abstraction makes large systems easier to organise,
   extend, and maintain.

9. Project Phoenix can use AIService as a common interface
   for multiple AI systems.


FINAL MEMORY RULE:

    Abstraction = WHAT

    Implementation = HOW

    Polymorphism = SAME INTERFACE, DIFFERENT BEHAVIOUR
"""


# ============================================================
# LESSON 23 COMPLETE
# ============================================================