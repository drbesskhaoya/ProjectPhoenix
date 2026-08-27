# PROJECT PHOENIX — LESSON 28

# PANDAS FUNDAMENTALS

# ============================================================

# TOPICS

# ============================================================

#

# 1. What is Pandas?

# 2. Importing Pandas

# 3. Creating a DataFrame

# 4. Understanding rows, columns, and indexes

# 5. Selecting one column

# 6. Selecting multiple columns

# 7. Selecting rows with iloc

# 8. Inspecting a DataFrame

# 9. Mini Project: Patient DataFrame

# 10. Key Takeaways

#

# ============================================================

# 1. WHAT IS PANDAS?

# ============================================================

#

# Pandas is a Python library used for working with structured,

# tabular data.

#

# A table might contain:

# - Patient information

# - Laboratory results

# - Hospital records

# - Financial data

# - Research datasets

#

# NumPy is particularly useful for numerical arrays.

# Pandas is particularly useful for structured tables.

#

# The main Pandas structure we use in this lesson is a DataFrame.

#

# ============================================================

# 2. IMPORTING PANDAS

# ============================================================

import pandas as pd

# "pd" is the conventional short name (alias) for Pandas.

#

# We can now use Pandas through "pd".

#

# Example:

# pd.DataFrame()

#

# ============================================================

# 3. CREATING A DATAFRAME

# ============================================================

#

# A DataFrame is a table containing rows and columns.

#

# We can create one from a Python dictionary.

#

# Each dictionary key becomes a column.

# Each list becomes the data inside that column.

data = {
"Patient": ["Ann", "James", "Sara"],
"Age": [25, 30, 35],
"Diagnosis": ["Hypertension", "Malaria", "Leukemia"]
}

df = pd.DataFrame(data)

print(df)

# Expected structure:

#

# Patient  Age     Diagnosis

# 0 Ann      25      Hypertension

# 1 James    30      Malaria

# 2 Sara     35      Leukemia

#

# Pandas automatically creates an index:

# 0

# 1

# 2

#

# ============================================================

# 4. ROWS, COLUMNS, AND INDEX

# ============================================================

#

# A DataFrame contains:

#

# - Rows     → individual records

# - Columns  → variables or fields

# - Index    → labels identifying rows

#

# In a healthcare dataset:

#

# Row     → one patient

# Column  → information about the patient

#

# Example:

#

# Patient | Age | Diagnosis

# --------|-----|-----------

# Ann     | 25  | Hypertension

#

# Here:

# - Ann is a patient record

# - Age is a variable

# - Diagnosis is a variable

# - 0 is the row index

#

# ============================================================

# 5. SELECTING ONE COLUMN

# ============================================================

#

# We can select one column using its name inside square brackets.

print(df["Age"])

# This returns a Pandas Series.

#

# A Series is essentially a single column of data.

#

# Example output:

#

# 0    25

# 1    30

# 2    35

#

# Name: Age

#

# ============================================================

# 6. SELECTING MULTIPLE COLUMNS

# ============================================================

#

# To select multiple columns, we provide a list of column names.

#

# Notice the double square brackets.

print(df[["Patient", "Age"]])

# The inner brackets create a Python list:

#

# ["Patient", "Age"]

#

# The outer brackets select those columns from the DataFrame.

#

# The result is another DataFrame.

#

# Important distinction:

#

# df["Age"]           → Series

# df[["Age"]]         → DataFrame

#

# ============================================================

# 7. SELECTING ROWS WITH ILOC

# ============================================================

#

# .iloc[] selects rows based on their numerical position.

#

# Python uses zero-based indexing:

#

# Position 0 → first row

# Position 1 → second row

# Position 2 → third row

#

# Example:

print(df.iloc[1])

# This selects the second row.

#

# For our dataset:

#

# Patient     James

# Age         30

# Diagnosis   Malaria

#

# .iloc[3] would select the fourth row if one exists.

#

# ============================================================

# 8. INSPECTING A DATAFRAME

# ============================================================

#

# Before analysing a dataset, we should inspect its structure.

#

# Pandas provides several useful tools.

#

# ------------------------------------------------------------

# head()

# ------------------------------------------------------------

#

# df.head() displays the first few rows.

print(df.head())

# ------------------------------------------------------------

# shape

# ------------------------------------------------------------

#

# df.shape tells us the number of rows and columns.

#

# The format is:

#

# (rows, columns)

print(df.shape)

# Example:

#

# (3, 3)

#

# This means:

# 3 rows

# 3 columns

#

# ------------------------------------------------------------

# columns

# ------------------------------------------------------------

#

# df.columns shows the names of the columns.

print(df.columns)

# ------------------------------------------------------------

# info()

# ------------------------------------------------------------

#

# df.info() gives us a structural summary of the DataFrame.

#

# It can show:

# - Number of rows

# - Column names

# - Number of non-null values

# - Data types

# - Memory usage

df.info()

# This is particularly useful when beginning work with

# a real healthcare dataset.

#

# ============================================================

# PRACTICE

# ============================================================

#

# Create a DataFrame containing:

#

# Patient:

# Amina, John, Mary

#

# Age:

# 42, 35, 58

#

# Diagnosis:

# Hypertension, Diabetes, Asthma

#

# Then:

#

# 1. Print the DataFrame.

# 2. Print only the Age column.

# 3. Print Patient and Diagnosis.

# 4. Print the second patient's row using iloc.

# 5. Print the shape.

# 6. Print the column names.

# 7. Use info() to inspect the DataFrame.

#

# ============================================================

# MINI PROJECT — PATIENT DATAFRAME

# ============================================================

#

# Create a small healthcare dataset containing four patients.

#

# Requirements:

#

# - Patient names

# - Ages

# - Diagnoses

#

# Then:

#

# 1. Create a DataFrame.

# 2. Print the complete DataFrame.

# 3. Print only the Patient column.

# 4. Print Patient and Diagnosis.

# 5. Select the fourth patient using iloc.

# 6. Print the shape.

# 7. Inspect the DataFrame using info().

#

# Example solution:

patient_data = {
"Patient": ["Ann", "James", "Sara", "David"],
"Age": [25, 30, 35, 50],
"Diagnosis": ["Hypertension", "Malaria", "Leukemia", "Diabetes"]
}

patient_df = pd.DataFrame(patient_data)

print(patient_df)

print(patient_df["Patient"])

print(patient_df[["Patient", "Diagnosis"]])

print(patient_df.iloc[3])

print(patient_df.shape)

patient_df.info()

# ============================================================

# KEY TAKEAWAYS

# ============================================================

#

# 1. Pandas is a Python library for working with structured data.

#

# 2. A DataFrame is Pandas' main table structure.

#

# 3. A Series represents a single column or a selected row.

#

# 4. A dictionary can be converted into a DataFrame using:

#

# pd.DataFrame(data)

#

# 5. Select one column with:

#

# df["Age"]

#

# 6. Select multiple columns with:

#

# df[["Patient", "Age"]]

#

# 7. Select a row by position with:

#

# df.iloc[1]

#

# 8. Inspect the first rows with:

#

# df.head()

#

# 9. Check the dimensions with:

#

# df.shape

#

# 10. Check column names with:

#

# df.columns

#

# 11. Inspect the DataFrame structure with:

#

# df.info()

#

# ============================================================

# END OF LESSON 28

# ============================================================
