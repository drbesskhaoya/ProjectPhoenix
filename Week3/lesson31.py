# ============================================================
# PROJECT PHOENIX — LESSON 31
# DATA VISUALIZATION
# ============================================================
#
# Topics:
# 1. Why visualize data?
# 2. Installing and importing Matplotlib
# 3. Bar charts
# 4. Titles and axis labels
# 5. Line charts
# 6. Scatter plots
# 7. Relationship vs causation
# 8. Choosing the right chart
# 9. Pandas + Matplotlib
# 10. Mini Project — Patient Diagnosis Visualization
#
# ============================================================


# ============================================================
# 1. WHY VISUALIZE DATA?
# ============================================================

# Data can be difficult to understand when presented only
# as numbers and tables.
#
# Visualization helps us see patterns quickly.
#
# General workflow:
#
# Raw Data
#     ↓
# Pandas
#     ↓
# Analyse
#     ↓
# Matplotlib
#     ↓
# Visualize
#     ↓
# Identify Patterns


# ============================================================
# 2. IMPORT MATPLOTLIB
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 3. BAR CHARTS
# ============================================================

# Bar charts are useful for comparing categories.

diagnoses = [
    "Hypertension",
    "Malaria",
    "Diabetes",
    "Leukemia"
]

patients = [2, 2, 2, 1]

plt.bar(diagnoses, patients)

plt.title("Patients by Diagnosis")
plt.xlabel("Diagnosis")
plt.ylabel("Number of Patients")

plt.show()


# ------------------------------------------------------------
# BAR CHART RULE
# ------------------------------------------------------------
#
# Bar chart → compare categories
#
# Examples:
# - Diagnosis vs number of patients
# - Department vs number of patients
# - Treatment type vs number of patients


# ============================================================
# 4. LINE CHARTS
# ============================================================

# Line charts are useful for showing trends or changes
# over time.

hours = [8, 10, 12, 14, 16, 18]

temperature = [
    37.1,
    37.3,
    37.8,
    38.2,
    38.5,
    38.1
]

plt.plot(hours, temperature)

plt.title("Patient Temperature Over Time")
plt.xlabel("Hour")
plt.ylabel("Temperature (°C)")

plt.show()


# ------------------------------------------------------------
# LINE CHART RULE
# ------------------------------------------------------------
#
# Line chart → show trends or change over time
#
# Examples:
# - Temperature over several hours
# - Blood pressure over several days
# - Patient weight over several months
# - Monthly hospital admissions


# ============================================================
# 5. SCATTER PLOTS
# ============================================================

# Scatter plots help us examine the relationship between
# two numerical variables.

age = [25, 32, 40, 48, 55, 63, 70]

systolic_bp = [
    110,
    115,
    120,
    128,
    135,
    142,
    150
]

plt.scatter(age, systolic_bp)

plt.title("Age vs Systolic Blood Pressure")
plt.xlabel("Age (years)")
plt.ylabel("Systolic Blood Pressure (mmHg)")

plt.show()


# ------------------------------------------------------------
# SCATTER PLOT RULE
# ------------------------------------------------------------
#
# Scatter plot → examine relationships between two
# numerical variables.
#
# Examples:
# - Age vs blood pressure
# - Age vs heart rate
# - Weight vs blood glucose
# - Height vs weight


# ============================================================
# 6. RELATIONSHIP DOES NOT AUTOMATICALLY MEAN CAUSATION
# ============================================================

# A scatter plot can show that two variables are related.
#
# For example, in our dataset:
#
# As age increases, systolic blood pressure tends to increase.
#
# However, this does NOT automatically prove that age causes
# the increase.
#
# Other variables may influence blood pressure.
#
# Important principle:
#
# Relationship ≠ Causation


# ============================================================
# 7. CHOOSING THE RIGHT CHART
# ============================================================

# Question:
#
# "Which diagnosis is most common?"
#
# → BAR CHART
#
#
# Question:
#
# "How does a patient's temperature change over 12 hours?"
#
# → LINE CHART
#
#
# Question:
#
# "Is age related to heart rate?"
#
# → SCATTER PLOT


# Quick reference:
#
# BAR
# ↓
# Compare categories
#
# LINE
# ↓
# Show trends/change over time
#
# SCATTER
# ↓
# Examine relationships between numerical variables


# ============================================================
# 8. PANDAS + MATPLOTLIB
# ============================================================

# Pandas can analyse the data.
# Matplotlib can visualize the analysis.
#
# Workflow:
#
# Pandas → analyse
# Matplotlib → visualize


data = {
    "Patient": [
        "Ann",
        "James",
        "Sara",
        "David",
        "Mary",
        "Peter",
        "Jane"
    ],

    "Age": [
        25,
        30,
        35,
        50,
        42,
        61,
        55
    ],

    "Diagnosis": [
        "Hypertension",
        "Malaria",
        "Leukemia",
        "Diabetes",
        "Malaria",
        "Diabetes",
        "Hypertension"
    ]
}

df = pd.DataFrame(data)

print("\nPATIENT DATA")
print(df)


# ============================================================
# 9. ANALYSE THE DATA WITH PANDAS
# ============================================================

diagnosis_counts = df["Diagnosis"].value_counts()

print("\nDIAGNOSIS COUNTS")
print(diagnosis_counts)


# ============================================================
# 10. VISUALIZE THE PANDAS RESULTS
# ============================================================

# diagnosis_counts.index
# → diagnosis names
#
# diagnosis_counts.values
# → corresponding patient counts

plt.bar(
    diagnosis_counts.index,
    diagnosis_counts.values
)

plt.title("Patients by Diagnosis")
plt.xlabel("Diagnosis")
plt.ylabel("Number of Patients")

plt.show()


# ============================================================
# 11. MINI PROJECT — PATIENT DIAGNOSIS VISUALIZATION
# ============================================================

# Objective:
#
# Create patient data
#       ↓
# Create DataFrame
#       ↓
# Count diagnoses
#       ↓
# Visualize diagnosis counts
#
# This combines our pandas skills from previous lessons
# with our new Matplotlib skills.


# ============================================================
# 12. KEY TAKEAWAYS
# ============================================================

# Matplotlib import:
#
# import matplotlib.pyplot as plt
#
#
# Bar chart:
#
# plt.bar(x, y)
#
# Used to compare categories.
#
#
# Line chart:
#
# plt.plot(x, y)
#
# Used to show trends/change over time.
#
#
# Scatter plot:
#
# plt.scatter(x, y)
#
# Used to examine relationships between numerical variables.
#
#
# Chart labels:
#
# plt.title()
# plt.xlabel()
# plt.ylabel()
# plt.show()
#
#
# MOST IMPORTANT PRINCIPLE:
#
# Choose the visualization based on the question
# you are asking of the data.
#
#
# PROJECT PHOENIX WORKFLOW:
#
# Pandas
#   ↓
# Analyse
#   ↓
# Matplotlib
#   ↓
# Visualize
#   ↓
# Understand patterns