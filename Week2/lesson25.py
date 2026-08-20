# ============================================================
# PROJECT PHOENIX - LESSON 25
# Dataclasses & Structured Healthcare Data
# ============================================================

"""
LEARNING OBJECTIVES
-------------------
By the end of this lesson, you should understand:

1. What a dataclass is
2. Why structured data is useful
3. How to create a dataclass
4. How to use type annotations
5. How to use default values
6. How to retrieve and update data
7. How to add methods to a dataclass
8. How dataclasses can represent healthcare records
"""


# ============================================================
# 1. WHY STRUCTURED DATA?
# ============================================================

"""
Healthcare systems contain many pieces of related information.

For example, a patient may have:

- Patient ID
- Name
- Age
- Diagnosis
- Blood pressure
- Medication

We could store these as separate variables, but that becomes
difficult to manage when we have many patients.

A better approach is to group related information into a
structured object.

A dataclass provides a convenient way to do this.
"""


# ============================================================
# 2. IMPORTING DATACLASS
# ============================================================

from dataclasses import dataclass


# ============================================================
# 3. CREATING A PATIENT DATACLASS
# ============================================================

@dataclass
class Patient:
    patient_id: str
    name: str
    age: int
    diagnosis: str


"""
The Patient dataclass is a blueprint.

Each Patient object will contain:

- patient_id
- name
- age
- diagnosis
"""


# ============================================================
# 4. TYPE ANNOTATIONS
# ============================================================

"""
The fields contain type annotations.

str  = text
int  = whole number
float = decimal number
bool = True or False

Examples:

name: str
age: int
"""

# Type annotations describe the expected type of data.
# They do not automatically prevent incorrect types.


# ============================================================
# 5. CREATING A PATIENT OBJECT
# ============================================================

patient1 = Patient(
    patient_id="P001",
    name="Amina",
    age=42,
    diagnosis="Hypertension"
)


# ============================================================
# 6. RETRIEVING DATA
# ============================================================

print(patient1.name)
print(patient1.age)
print(patient1.diagnosis)

"""
Expected output:

Amina
42
Hypertension
"""


# ============================================================
# 7. DEFAULT VALUES
# ============================================================

@dataclass
class PatientWithDefault:
    patient_id: str
    name: str
    age: int
    diagnosis: str = "Not yet diagnosed"


"""
A default value is useful when information is not available yet.
"""

patient2 = PatientWithDefault(
    patient_id="P002",
    name="John",
    age=35
)

print(patient2)

"""
Expected output:

PatientWithDefault(
    patient_id='P002',
    name='John',
    age=35,
    diagnosis='Not yet diagnosed'
)
"""

"""
RULE:

A supplied value overrides the default value.
"""

patient3 = PatientWithDefault(
    patient_id="P003",
    name="Mary",
    age=50,
    diagnosis="Diabetes"
)

print(patient3.diagnosis)

"""
Expected output:

Diabetes
"""


# ============================================================
# 8. UPDATING DATA
# ============================================================

patient2.diagnosis = "Hypertension"
patient2.age = 36

print(patient2.diagnosis)
print(patient2.age)

"""
The existing object has been updated.

We did not create a new patient.
We changed information stored in the existing object.
"""


# ============================================================
# 9. ADDING METHODS TO A DATACLASS
# ============================================================

@dataclass
class ClinicalPatient:
    patient_id: str
    name: str
    age: int
    diagnosis: str = "Not yet diagnosed"

    def summary(self):
        return f"{self.name} ({self.age}) - {self.diagnosis}"


"""
A dataclass can contain methods just like a normal class.

The method above creates a short patient summary.
"""


patient4 = ClinicalPatient(
    patient_id="P004",
    name="Amina",
    age=42,
    diagnosis="Hypertension"
)

print(patient4.summary())

"""
Expected output:

Amina (42) - Hypertension
"""


# ============================================================
# 10. UNDERSTANDING self
# ============================================================

"""
Inside a method, self refers to the particular object using
the method.

For example:

patient4.name

contains:

Amina

Therefore, inside patient4.summary():

self.name

refers to:

Amina

Different objects can use the same method while working with
their own data.
"""


# ============================================================
# 11. MINI PROJECT - PATIENT REGISTRY
# ============================================================

@dataclass
class PatientRecord:
    patient_id: str
    name: str
    age: int
    diagnosis: str = "Not yet diagnosed"

    def summary(self):
        return f"{self.name} ({self.age}) - {self.diagnosis}"


patient1 = PatientRecord(
    patient_id="P001",
    name="Amina",
    age=42,
    diagnosis="Hypertension"
)

patient2 = PatientRecord(
    patient_id="P002",
    name="John",
    age=35
)

patient3 = PatientRecord(
    patient_id="P003",
    name="Mary",
    age=50,
    diagnosis="Diabetes"
)


print(patient1.summary())
print(patient2.summary())
print(patient3.summary())

"""
Expected output:

Amina (42) - Hypertension
John (35) - Not yet diagnosed
Mary (50) - Diabetes
"""


# ============================================================
# 12. DATACLASS VS REGULAR CLASS
# ============================================================

"""
A regular class might require us to write:

class Patient:

    def __init__(self, patient_id, name, age, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis


A dataclass allows us to define the structure more concisely:

@dataclass
class Patient:
    patient_id: str
    name: str
    age: int
    diagnosis: str


The dataclass automatically handles much of the repetitive
setup.
"""


# ============================================================
# 13. HEALTHCARE APPLICATION
# ============================================================

"""
Dataclasses can represent many types of healthcare information:

- Patient records
- Medication records
- Laboratory results
- Vital signs
- Appointments
- Clinical observations
- AI predictions
- Risk assessments
- Medical reports
"""


@dataclass
class VitalSigns:
    temperature: float
    heart_rate: int
    systolic_bp: int
    diastolic_bp: int


vitals = VitalSigns(
    temperature=38.2,
    heart_rate=105,
    systolic_bp=145,
    diastolic_bp=90
)

print(vitals.temperature)
print(vitals.heart_rate)

"""
Expected output:

38.2
105
"""


# ============================================================
# 14. PRACTICE CHALLENGES
# ============================================================

"""
CHALLENGE 1
-----------

Create a Doctor dataclass with:

- doctor_id
- name
- specialty

Use appropriate type annotations.


CHALLENGE 2
-----------

Create a LabResult dataclass with:

- test_name
- result
- unit


CHALLENGE 3
-----------

Add a method called display() to LabResult.

It should return a readable result such as:

Haemoglobin: 13.5 g/dL


CHALLENGE 4
-----------

Create three Patient objects and print their summaries.
"""


# ============================================================
# 15. KEY TAKEAWAYS
# ============================================================

"""
1. Dataclasses organize related data.

2. Type annotations describe expected data types.

3. Default values provide automatic values when information
   is not supplied.

4. Dataclass fields can be retrieved easily using dot notation.

5. Dataclass fields can be updated.

6. Dataclasses can contain methods.

7. Dataclasses automatically provide a useful representation
   when printed.

8. Dataclasses are useful for representing structured
   healthcare data.
"""


# ============================================================
# 16. PROJECT PHOENIX CONNECTION
# ============================================================

"""
Our Python journey is becoming more advanced:

Variables
    |
Lists
    |
Dictionaries
    |
Functions
    |
Classes
    |
Inheritance
    |
Polymorphism
    |
Dataclasses
    |
Structured Healthcare Data


The important transition is from basic Python syntax toward
designing structures that can represent real-world healthcare
data and eventually support healthcare AI systems.
"""


# ============================================================
# LESSON 25 FINAL CONCEPT
# ============================================================

"""
A dataclass provides a clean blueprint for grouping related
data into structured objects, while allowing those objects
to contain useful behavior through methods.

Healthcare example:

Patient
    |
    +-- patient_id
    +-- name
    +-- age
    +-- diagnosis
    |
    +-- summary()


This makes healthcare data easier to organize, retrieve,
update, and use in larger Python applications.

END OF LESSON 25
"""