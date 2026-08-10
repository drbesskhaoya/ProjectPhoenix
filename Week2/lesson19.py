# ============================================================

# PROJECT PHOENIX — WEEK 2

# LESSON 19: OOP PART 2 — INHERITANCE

# Healthcare AI Engineering Track

# ============================================================

"""
LESSON 19 — OBJECT-ORIENTED PROGRAMMING: INHERITANCE

Topics:

1. The problem inheritance solves
2. Parent classes
3. Child classes
4. Creating a child class
5. Inheriting attributes and methods
6. Reusing parent functionality
7. super()
8. Extending a parent class
9. Method overriding
10. IS-A relationships
11. When inheritance makes sense
12. When NOT to use inheritance
13. Common inheritance mistakes
14. Clean class hierarchy design
15. Healthcare applications of inheritance
16. Hospital Management System architecture
17. Healthcare AI architecture connections

============================================================
PART 1 — THE PROBLEM INHERITANCE SOLVES
=======================================

Without inheritance, we may duplicate the same code in multiple
classes.

For example, both Patient and Doctor are people.

They may both need:

```
name
age
introduce()
```

Duplicating this functionality across many classes creates:

```
- Repeated code
- Harder maintenance
- Greater risk of inconsistency
```

Inheritance allows shared functionality to be placed in a
parent class and reused by child classes.

============================================================
PART 2 — PARENT AND CHILD CLASSES
=================================

A PARENT CLASS contains functionality that is common to other
classes.

A CHILD CLASS inherits functionality from the parent and can
also add its own specialised functionality.

Example:

```
                Person
               /      \
              /        \
         Patient      Doctor
```

Person = parent class
Patient = child class
Doctor = child class

The relationship is:

```
Patient IS A Person
Doctor IS A Person
```

============================================================
PART 3 — CREATING A PARENT CLASS
================================

"""

class Person:
def **init**(self, name, age):
self.name = name
self.age = age

```
def introduce(self):
    print(f"My name is {self.name}.")
```

"""
Person contains functionality shared by different types of
people.

Common attributes:

```
name
age
```

Common method:

```
introduce()
```

============================================================
PART 4 — CREATING A CHILD CLASS
===============================

A child class inherits from a parent using parentheses:

```
class Patient(Person):
```

The parent class is written inside the parentheses.
"""

class Patient(Person):
pass

"""
Patient now inherits:

```
name
age
introduce()
```

from Person.

Example:

```
patient1 = Patient("Mary", 45)
patient1.introduce()
```

Output:

```
My name is Mary.
```

============================================================
PART 5 — INHERITING ATTRIBUTES AND METHODS
==========================================

A child class can use attributes and methods defined by its
parent.

Patient does not need to redefine:

```
name
age
introduce()
```

The inherited method can be used directly.
"""

patient1 = Patient("Mary", 45)

print(patient1.name)
print(patient1.age)

patient1.introduce()

# """

# PART 6 — EXTENDING A PARENT CLASS

A child class often needs additional information that does not
belong in the parent.

For example:

Person:
name
age

Patient:
patient_id

The child can extend the parent by adding its own attributes.

============================================================
PART 7 — super()
================

When a child defines its own **init**(), it can use super() to
call the parent's **init**().

Example:

```
super().__init__(name, age)
```

This means:

```
"Parent class, initialise the Person-related information."
```

This prevents duplication.

"""

class Patient(Person):
def **init**(self, name, age, patient_id):
super().**init**(name, age)
self.patient_id = patient_id

patient1 = Patient("Mary", 45, "P001")

print(patient1.name)
print(patient1.age)
print(patient1.patient_id)

"""
The parent handles:

```
name
age
```

The child handles:

```
patient_id
```

============================================================
PART 8 — METHOD OVERRIDING
==========================

A child class can create its own version of a method that
already exists in the parent.

This is called METHOD OVERRIDING.

When a child object calls an overridden method, Python uses the
child's version.

Example:

```
Person
    introduce()

Patient
    introduce()
```

Patient's version takes precedence for Patient objects.
"""

class Person:
def **init**(self, name, age):
self.name = name
self.age = age

```
def introduce(self):
    print("I am a person.")
```

class Patient(Person):
def introduce(self):
print("I am a patient.")

person1 = Person("John", 40)
patient1 = Patient("Mary", 45)

person1.introduce()
patient1.introduce()

"""
Output:

```
I am a person.
I am a patient.
```

============================================================
PART 9 — USING super() WITH OVERRIDDEN METHODS
==============================================

A child can override a method while still using the parent's
version.

Example:

```
super().introduce()
```

This allows the child to reuse the parent's behaviour and then
add specialised behaviour.

"""

class Person:
def **init**(self, name, age):
self.name = name
self.age = age

```
def introduce(self):
    print(f"My name is {self.name}.")
```

class Patient(Person):
def **init**(self, name, age, patient_id):
super().**init**(name, age)
self.patient_id = patient_id

```
def introduce(self):
    super().introduce()
    print(f"My patient ID is {self.patient_id}.")
```

patient1 = Patient("Mary", 45, "P001")
patient1.introduce()

"""
Output:

```
My name is Mary.
My patient ID is P001.
```

The sequence is:

```
Patient.introduce()
        ↓
super().introduce()
        ↓
Person.introduce()
        ↓
Patient continues
        ↓
Patient-specific information
```

============================================================
PART 10 — DOCTOR CHILD CLASS
============================

A Doctor is also a Person.

Doctor can inherit:

```
name
age
introduce()
```

Doctor can add:

```
doctor_id
specialty
```

"""

class Doctor(Person):
def **init**(self, name, age, doctor_id, specialty):
super().**init**(name, age)
self.doctor_id = doctor_id
self.specialty = specialty

```
def introduce(self):
    super().introduce()
    print(
        f"My doctor ID is {self.doctor_id}. "
        f"My specialty is {self.specialty}."
    )
```

doctor1 = Doctor(
"Dr. Kamau",
38,
"D001",
"Cardiology"
)

doctor1.introduce()

"""
Output:

```
My name is Dr. Kamau.
My doctor ID is D001. My specialty is Cardiology.
```

============================================================
PART 11 — IS-A RELATIONSHIPS
============================

Inheritance usually represents an IS-A relationship.

Examples:

```
Patient IS A Person
Doctor IS A Person
Nurse IS A Person
Administrator IS A Person
```

This makes inheritance conceptually appropriate.

============================================================
PART 12 — HAS-A RELATIONSHIPS
=============================

Not every relationship should use inheritance.

Examples:

```
Patient HAS A MedicalRecord
Patient HAS AN Appointment
Patient HAS A Prescription
Doctor HAS A Schedule
```

These are HAS-A relationships.

They should generally be represented using composition or
association rather than inheritance.

Do NOT create:

```
class Patient(MedicalRecord):
```

because:

```
Patient IS NOT A MedicalRecord.
```

Instead, conceptually:

```
Patient
   |
   └── MedicalRecord
```

============================================================
PART 13 — WHEN INHERITANCE MAKES SENSE
======================================

Inheritance is appropriate when:

1. There is a genuine IS-A relationship.

2. The child is a specialised version of the parent.

3. The child genuinely needs functionality from the parent.

4. The parent contains functionality that is genuinely common
   to its children.

Examples:

```
Person → Patient
Person → Doctor
Person → Nurse
```

============================================================
PART 14 — WHEN NOT TO USE INHERITANCE
=====================================

Do NOT use inheritance merely because two classes:

```
- have something in common
- share an attribute
- need to communicate
- are related in the hospital
```

For example:

```
Patient → Appointment
```

is not inheritance.

A patient HAS an appointment.

Also avoid inheritance when it creates an artificial hierarchy.

Ask:

```
"Can I truthfully say X IS A Y?"
```

If not, inheritance may not be appropriate.

============================================================
PART 15 — COMMON INHERITANCE MISTAKES
=====================================

MISTAKE 1 — Duplicating the parent's initialization

Bad:

```
class Patient(Person):
    def __init__(self, name, age, patient_id):
        self.name = name
        self.age = age
        self.patient_id = patient_id
```

Better:

```
class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id
```

MISTAKE 2 — Forgetting super()

If the child defines its own **init**(), the parent's
**init**() does not automatically run.

If the child needs the parent's initialization, use:

```
super().__init__(...)
```

MISTAKE 3 — Putting specialised attributes in the parent

Do not put:

```
patient_id
doctor_id
specialty
```

inside Person.

They belong to their specialised child classes.

MISTAKE 4 — Using inheritance for HAS-A relationships

Patient HAS A MedicalRecord.

Patient is NOT a MedicalRecord.

MISTAKE 5 — Creating overly complicated hierarchies

Inheritance should simplify the system, not make it harder
to understand.

============================================================
PART 16 — CLEAN CLASS HIERARCHY DESIGN
======================================

A clean hospital hierarchy might look like:

```
                Person
          /       |       \
         ↓        ↓        ↓
     Patient    Doctor    Nurse
```

Later:

```
                Person
      /       /      |       \
     ↓       ↓       ↓        ↓
Patient   Doctor   Nurse   Administrator
```

Person should contain only genuinely shared functionality:

```
name
age
introduce()
```

Patient can contain:

```
patient_id
```

Doctor can contain:

```
doctor_id
specialty
```

Nurse can contain:

```
nurse_id
department
```

Administrator can contain:

```
employee_id
```

Do not put every possible hospital attribute into Person.

============================================================
PART 17 — HEALTHCARE APPLICATION
================================

Inheritance reflects real-world healthcare roles.

For example:

```
Person
   |
   ├── Patient
   ├── Doctor
   ├── Nurse
   └── Administrator
```

All are people but have different responsibilities.

The parent provides common functionality.

The children provide specialised functionality.

============================================================
PART 18 — HOSPITAL MANAGEMENT SYSTEM CONNECTION
===============================================

In Project Phoenix, inheritance can eventually help organise
different types of people interacting with the hospital system.

For example:

```
Person
   |
   ├── Patient
   ├── Doctor
   ├── Nurse
   └── Administrator
```

Patient may have:

```
patient_id
medical_record
appointments
```

Doctor may have:

```
doctor_id
specialty
schedule
```

Nurse may have:

```
nurse_id
department
shift
```

Administrator may have:

```
employee_id
department
```

IMPORTANT:

MedicalRecord, Appointment, Prescription, etc. are NOT
necessarily subclasses of Patient.

They are associated with Patient objects.

For example:

```
Patient HAS A MedicalRecord
Patient HAS AN Appointment
Patient HAS A Prescription
```

============================================================
PART 19 — HEALTHCARE AI CONNECTION
==================================

Inheritance is one part of a larger software architecture.

A future Healthcare AI system might look conceptually like:

```
Patient
   ↓
MedicalRecord
   ↓
ClinicalData
   ↓
Data Processing
   ↓
AI Model
   ↓
Prediction / Risk Score
   ↓
Clinician
```

Inheritance helps organise the different types of entities
in the system.

However, AI functionality should not be forced into one giant
Patient class.

Good architecture separates responsibilities.

For example:

```
Patient
    = represents the patient

MedicalRecord
    = represents clinical records

AIModel / AIService
    = performs AI-related processing
```

This separation makes the system easier to test, maintain,
and eventually scale.

============================================================
PART 20 — SENIOR ENGINEER PRINCIPLES
====================================

Remember these rules:

1. Use inheritance for genuine IS-A relationships.

2. Use composition/association for HAS-A relationships.

3. Put common functionality in the parent.

4. Put specialised functionality in the child.

5. Use super() to reuse parent functionality.

6. Avoid duplicating parent initialization.

7. Do not create inheritance hierarchies simply for code reuse.

8. Keep parent classes focused and general.

9. Keep child classes specialised.

10. Prefer simple, understandable architecture.

============================================================
PART 21 — MINI PROJECT
======================

Build a small Hospital People System.

Requirements:

Person:
- name
- age
- introduce()

Patient:
- inherits Person
- patient_id
- overrides introduce()
- uses super()

Doctor:
- inherits Person
- doctor_id
- specialty
- overrides introduce()
- uses super()

Example:

```
patient1 = Patient("Mary", 45, "P001")

doctor1 = Doctor(
    "Dr. Kamau",
    38,
    "D001",
    "Cardiology"
)
```

Expected behaviour:

```
My name is Mary.
My patient ID is P001

My name is Dr. Kamau.
My doctor ID is D001. My specialty is Cardiology.
```

============================================================
PART 22 — FINAL LESSON 19 SUMMARY
=================================

Inheritance allows a child class to reuse functionality from
a parent class.

The basic syntax is:

```
class Child(Parent):
```

A child can inherit:

```
- attributes
- methods
```

A child can extend the parent by adding its own functionality.

super() allows the child to call functionality from the parent.

Example:

```
super().__init__(name, age)
```

Method overriding allows a child to provide its own version of
a parent's method.

The most important relationship rule is:

```
IS-A → inheritance

HAS-A → composition/association
```

Healthcare example:

```
                Person
          /       |       \
         ↓        ↓        ↓
     Patient    Doctor    Nurse
```

This architecture can eventually support a larger Hospital
Management System and Healthcare AI software architecture.

============================================================
KEY TAKEAWAYS
=============

1. Inheritance prevents unnecessary duplication.

2. Parent classes contain common functionality.

3. Child classes contain specialised functionality.

4. A child can inherit attributes and methods from a parent.

5. super() allows a child to reuse parent functionality.

6. Method overriding allows specialised child behaviour.

7. Patient IS A Person.

8. Doctor IS A Person.

9. Patient HAS A MedicalRecord.

10. Patient HAS AN Appointment.

11. Not every relationship should use inheritance.

12. Good inheritance creates clean and maintainable systems.

13. Healthcare software can use inheritance to model different
    types of people and roles.

14. Inheritance is one building block of larger Healthcare AI
    software architecture.

============================================================
END OF LESSON 19
================

"""

# ============================================================

# PROJECT PHOENIX — LESSON 19 COMPLETE

# ============================================================

# OOP PART 2 — INHERITANCE

#

# Next lesson: OOP Part 3

# ============================================================
