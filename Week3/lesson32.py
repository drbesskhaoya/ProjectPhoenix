# ============================================================
# PROJECT PHOENIX
# LESSON 32 — HEALTHCARE VISUALIZATION PROJECT
# ============================================================
#
# PROJECT:
# Clinical Dashboard — Vital Signs & Patient Outcomes
#
# PURPOSE:
# In this lesson we combine Pandas + Matplotlib to create
# meaningful visualizations from healthcare data.
#
# We are NOT learning basic plotting again.
# Lesson 31 already covered:
# - Matplotlib
# - line charts
# - bar charts
# - histograms
# - scatter plots
# - interpreting visualizations
#
# Lesson 32 is about applying those skills to a healthcare
# dataset and thinking like a healthcare data scientist.
#
# ============================================================


# ============================================================
# LESSON GOALS
# ============================================================
#
# By the end of this lesson, we should be able to:
#
# 1. Create a healthcare DataFrame.
# 2. Analyse clinical variables using Pandas.
# 3. Choose an appropriate visualization for a question.
# 4. Create several healthcare visualizations.
# 5. Compare clinical measurements.
# 6. Identify simple patterns in the data.
# 7. Interpret visualizations rather than simply creating them.
# 8. Combine several visualizations into a small clinical
#    dashboard-style project.
#
# The important skill is:
#
#        DATA
#          ↓
#      ANALYSIS
#          ↓
#   VISUALIZATION
#          ↓
#   INTERPRETATION
#
# ============================================================


# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================
#
# Pandas is used for:
# - creating the DataFrame
# - analysing the healthcare data
# - grouping and summarising data
#
# Matplotlib is used for:
# - creating visualizations
# - displaying the results of our analysis
#
# These libraries were already introduced in earlier lessons.
# We are applying them here rather than learning them again.
#
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 2. CREATE OUR HEALTHCARE DATASET
# ============================================================
#
# We will use a small fictional outpatient dataset.
#
# Variables:
#
# Patient       → patient name
# Age           → patient's age
# Diagnosis     → clinical diagnosis
# Systolic_BP   → systolic blood pressure
# Diastolic_BP  → diastolic blood pressure
# Heart_Rate    → heart rate
#
# NOTE:
# This is fictional teaching data.
# It must NOT be interpreted as real clinical evidence.
#
# ============================================================

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
    ],

    "Systolic_BP": [
        110,
        115,
        120,
        128,
        135,
        142,
        150
    ],

    "Diastolic_BP": [
        70,
        75,
        80,
        85,
        90,
        95,
        100
    ],

    "Heart_Rate": [
        60,
        65,
        70,
        75,
        80,
        85,
        90
    ]
}


df = pd.DataFrame(data)


# ============================================================
# 3. INSPECT THE DATASET
# ============================================================
#
# Before visualising healthcare data, we should understand
# what is actually inside the DataFrame.
#
# ============================================================

print("HEALTHCARE DATASET")
print(df)


# Check the dimensions of the DataFrame.
#
# Expected:
#
# (7, 6)
#
# This means:
# 7 rows
# 6 columns
#
# ============================================================

print("\nDATASET SHAPE")
print(df.shape)


# Display the column names.
#
# ============================================================

print("\nCOLUMN NAMES")
print(df.columns)


# Display basic information about the dataset.
#
# ============================================================

print("\nDATA TYPES")
print(df.dtypes)


# ============================================================
# 4. CLINICAL QUESTIONS
# ============================================================
#
# Instead of creating random charts, we will begin with
# questions.
#
# A healthcare data scientist should ask:
#
# "What am I trying to understand?"
#
# before asking:
#
# "Which chart should I make?"
#
# Our project questions are:
#
# Question 1:
# Which diagnoses are most common?
#
# Question 2:
# How does average age differ between diagnoses?
#
# Question 3:
# How do systolic and diastolic blood pressure compare
# between patients?
#
# Question 4:
# Is there an apparent relationship between age and
# systolic blood pressure?
#
# ============================================================


# ============================================================
# 5. VISUALIZATION 1 — DIAGNOSIS FREQUENCY
# ============================================================
#
# CLINICAL QUESTION:
#
# Which diagnoses are most represented in our dataset?
#
# Diagnosis is categorical data.
#
# A bar chart is therefore appropriate because it allows
# us to compare categories.
#
# We already learned value_counts() in Lesson 30.
# We are applying it here.
#
# ============================================================

diagnosis_counts = df["Diagnosis"].value_counts()

print("\nDIAGNOSIS COUNTS")
print(diagnosis_counts)


# Create the bar chart.
#
# ============================================================

diagnosis_counts.plot(kind="bar")

plt.title("Number of Patients by Diagnosis")
plt.xlabel("Diagnosis")
plt.ylabel("Number of Patients")

plt.tight_layout()
plt.show()


# ============================================================
# INTERPRETATION
# ============================================================
#
# In this dataset:
#
# Hypertension = 2 patients
# Malaria      = 2 patients
# Diabetes     = 2 patients
# Leukemia     = 1 patient
#
# Therefore:
#
# Hypertension, malaria and diabetes are equally represented.
#
# Leukemia has the lowest frequency.
#
# IMPORTANT:
#
# This does NOT mean leukemia is less common in the real
# population.
#
# We are looking at only seven fictional patients.
#
# This is an example of an important data science principle:
#
#       DATASET PATTERN ≠ POPULATION TRUTH
#
# ============================================================


# ============================================================
# 6. VISUALIZATION 2 — AVERAGE AGE BY DIAGNOSIS
# ============================================================
#
# CLINICAL QUESTION:
#
# How does the average age differ between diagnoses?
#
# We already learned groupby() and mean() in Lesson 30.
#
# We will combine those skills with visualization.
#
# ============================================================

age_by_diagnosis = df.groupby("Diagnosis")["Age"].mean()

print("\nAVERAGE AGE BY DIAGNOSIS")
print(age_by_diagnosis)


# Create the bar chart.
#
# ============================================================

age_by_diagnosis.plot(kind="bar")

plt.title("Average Age by Diagnosis")
plt.xlabel("Diagnosis")
plt.ylabel("Average Age")

plt.tight_layout()
plt.show()


# ============================================================
# INTERPRETATION
# ============================================================
#
# The chart allows us to compare the average age of patients
# within each diagnosis category.
#
# However, we should be careful.
#
# Some diagnoses have only one patient.
#
# For example:
#
# Leukemia has only one patient in this dataset.
#
# Therefore, its "average age" is simply that patient's age.
#
# This is why data scientists consider:
#
# - sample size
# - distribution
# - variability
# - clinical context
#
# before drawing conclusions.
#
# ============================================================


# ============================================================
# 7. VISUALIZATION 3 — BLOOD PRESSURE BY PATIENT
# ============================================================
#
# CLINICAL QUESTION:
#
# How do systolic and diastolic blood pressure measurements
# compare across our patients?
#
# We have two related numerical variables:
#
# Systolic BP
# Diastolic BP
#
# A grouped bar chart allows us to compare both measurements
# for each patient.
#
# ============================================================

df.plot(
    x="Patient",
    y=["Systolic_BP", "Diastolic_BP"],
    kind="bar"
)

plt.title("Blood Pressure by Patient")
plt.xlabel("Patient")
plt.ylabel("Blood Pressure (mmHg)")

plt.tight_layout()
plt.show()


# ============================================================
# INTERPRETATION
# ============================================================
#
# The chart allows us to compare:
#
# - systolic BP
# - diastolic BP
#
# for each patient.
#
# We can immediately see that the blood pressure values
# generally increase as we move through this particular
# dataset.
#
# However, the order of patients is simply the order in which
# they were entered into the DataFrame.
#
# A visualization should therefore always be interpreted in
# the context of how the data was collected and organised.
#
# ============================================================


# ============================================================
# 8. VISUALIZATION 4 — AGE VS SYSTOLIC BLOOD PRESSURE
# ============================================================
#
# CLINICAL QUESTION:
#
# Is there an apparent relationship between age and systolic
# blood pressure?
#
# We have two numerical variables:
#
# Age
# Systolic_BP
#
# A scatter plot is appropriate for exploring the relationship
# between two numerical variables.
#
# ============================================================

df.plot(
    x="Age",
    y="Systolic_BP",
    kind="scatter"
)

plt.title("Age vs Systolic Blood Pressure")
plt.xlabel("Age")
plt.ylabel("Systolic BP (mmHg)")

plt.tight_layout()
plt.show()


# ============================================================
# INTERPRETATION
# ============================================================
#
# The points in our small dataset show an upward pattern:
#
# older patients generally have higher systolic BP values.
#
# But we must NOT conclude that age causes higher blood
# pressure from this chart alone.
#
# Why?
#
# Because:
#
# - our dataset is extremely small
# - this is fictional data
# - correlation does not establish causation
# - other variables may influence blood pressure
#
# The scatter plot is therefore an exploratory tool.
#
# ============================================================


# ============================================================
# 9. ADDING A CLINICAL SUMMARY
# ============================================================
#
# A dashboard should not only show charts.
#
# We can also calculate useful summary information.
#
# Let's calculate:
#
# - average age
# - average systolic BP
# - average diastolic BP
# - average heart rate
#
# ============================================================

print("\nCLINICAL SUMMARY")

print("Average age:")
print(df["Age"].mean())

print("\nAverage systolic BP:")
print(df["Systolic_BP"].mean())

print("\nAverage diastolic BP:")
print(df["Diastolic_BP"].mean())

print("\nAverage heart rate:")
print(df["Heart_Rate"].mean())


# ============================================================
# 10. DESCRIPTIVE STATISTICS
# ============================================================
#
# Pandas can provide a statistical summary of numerical
# columns using describe().
#
# We already know the concept of summary statistics from
# previous lessons.
#
# Here we use the summary as part of our dashboard analysis.
#
# ============================================================

print("\nDESCRIPTIVE STATISTICS")

print(df.describe())


# ============================================================
# 11. COMBINING ANALYSIS AND VISUALIZATION
# ============================================================
#
# This is the central idea of Lesson 32.
#
# We are no longer simply learning:
#
# "How do I make a bar chart?"
#
# Instead, we are asking:
#
# "What clinical question can this chart help answer?"
#
#
# Example:
#
# Categorical data
#       ↓
# value_counts()
#       ↓
# bar chart
#       ↓
# diagnosis comparison
#
#
# Group comparison
#       ↓
# groupby()
#       ↓
# mean()
#       ↓
# bar chart
#       ↓
# compare average age
#
#
# Two numerical variables
#       ↓
# scatter plot
#       ↓
# explore relationship
#
# ============================================================


# ============================================================
# 12. MINI PROJECT — CLINICAL DASHBOARD
# ============================================================
#
# We now bring the lesson together.
#
# A simple clinical dashboard should provide several views
# of the same dataset.
#
# Our dashboard questions:
#
# 1. What diagnoses are present?
# 2. What is the age profile?
# 3. What are the blood pressure measurements?
# 4. Is there a visible relationship between age and BP?
#
# We already created each visualization separately above.
#
# In a real project, we could arrange these visualizations
# into a single dashboard using more advanced Matplotlib
# techniques.
#
# For this lesson, the four visualizations together represent
# our first dashboard-style healthcare analysis.
#
# ============================================================


# ============================================================
# 13. PRACTICE — DATA SCIENTIST THINKING
# ============================================================
#
# Practice Question 1:
#
# If we wanted to compare the number of patients in each
# diagnosis category, which chart would be appropriate?
#
# Answer:
# Bar chart.
#
#
# Practice Question 2:
#
# If we wanted to examine the distribution of patient ages,
# which chart would be appropriate?
#
# Answer:
# Histogram.
#
#
# Practice Question 3:
#
# If we wanted to examine the relationship between age and
# systolic BP, which chart would be appropriate?
#
# Answer:
# Scatter plot.
#
#
# Practice Question 4:
#
# If we wanted to compare systolic and diastolic BP between
# individual patients, which visualization could we use?
#
# Answer:
# Grouped bar chart.
#
#
# The important principle:
#
#       CHOOSE THE CHART BASED ON THE QUESTION.
#
# ============================================================


# ============================================================
# 14. WHAT WE HAVE BUILT
# ============================================================
#
# Our project now contains:
#
# 1. A healthcare DataFrame
#
# 2. Diagnosis frequency analysis
#
# 3. Average age by diagnosis
#
# 4. Blood pressure comparison
#
# 5. Age vs systolic BP scatter plot
#
# 6. Clinical summary statistics
#
# 7. Descriptive statistics
#
# Together, these form a small healthcare visualization
# project.
#
# ============================================================


# ============================================================
# 15. IMPORTANT DATA SCIENCE LESSON
# ============================================================
#
# Visualization is not decoration.
#
# A good visualization should help us:
#
# - compare
# - detect patterns
# - identify unusual observations
# - communicate findings
# - generate questions for further analysis
#
# In healthcare, this can support:
#
# - clinical audit
# - service evaluation
# - population health analysis
# - quality improvement
# - research
# - healthcare operations
# - clinical decision-support development
#
# But visualization does not replace clinical judgement or
# statistical analysis.
#
# ============================================================


# ============================================================
# 16. KEY TAKEAWAYS
# ============================================================
#
# 1. Pandas and Matplotlib work well together.
#
# 2. Start with a question before choosing a visualization.
#
# 3. Bar charts are useful for comparing categories.
#
# 4. Histograms are useful for examining distributions.
#
# 5. Scatter plots are useful for exploring relationships
#    between numerical variables.
#
# 6. groupby() can produce summaries that can then be
#    visualized.
#
# 7. A chart can reveal patterns, but a pattern is not
#    automatically a clinically meaningful finding.
#
# 8. Small datasets require cautious interpretation.
#
# 9. Visualization is part of communicating data insights.
#
# 10. The goal of healthcare data science is not simply to
#     produce charts — it is to extract and communicate useful
#     information from healthcare data.
#
# ============================================================


# ============================================================
# PROJECT PHOENIX PROGRESS
# ============================================================
#
# Lesson 26 → NumPy Fundamentals                 COMPLETE
# Lesson 27 → NumPy in Practice                  COMPLETE
# Lesson 28 → Pandas Fundamentals                COMPLETE
# Lesson 29 → Pandas Data Cleaning               COMPLETE
# Lesson 30 → Pandas Analysis                    COMPLETE
# Lesson 31 → Data Visualization                 COMPLETE
# Lesson 32 → Healthcare Visualization Project   COMPLETE
#