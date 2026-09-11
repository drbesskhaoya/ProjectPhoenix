# ============================================================
# PROJECT PHOENIX
# LESSON 33 — EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================

# ============================================================
# LESSON OBJECTIVES
# ============================================================

# By the end of this lesson, you should understand how to:
#
# 1. Understand a dataset before analyzing it
# 2. Inspect dataset structure and data types
# 3. Check for missing values
# 4. Check for duplicate records
# 5. Explore numerical variables
# 6. Explore categorical variables
# 7. Examine distributions and patterns
# 8. Identify possible outliers and anomalies
# 9. Explore relationships between variables
# 10. Generate preliminary observations and questions
#
# The main goal is NOT to memorize commands.
#
# The goal is to develop the EDA mindset:
#
#     Understand
#         ↓
#     Inspect
#         ↓
#     Check data quality
#         ↓
#     Describe
#         ↓
#     Explore
#         ↓
#     Compare
#         ↓
#     Investigate relationships
#         ↓
#     Identify anomalies
#         ↓
#     Generate questions
#
# ============================================================


# ============================================================
# PART 1 — WHAT IS EDA?
# ============================================================

# Exploratory Data Analysis (EDA) is the process of
# systematically investigating a dataset.
#
# EDA helps us:
#
# - understand the data
# - detect data-quality problems
# - identify patterns
# - understand distributions
# - compare groups
# - identify possible outliers
# - explore relationships
# - generate questions for further investigation
#
# EDA is NOT simply running Pandas commands.
#
# The important question is:
#
#     "What am I trying to understand about this data?"
#
# EDA is investigation.
#
# ============================================================


# ============================================================
# PART 2 — IMPORT PANDAS
# ============================================================

import pandas as pd


# ============================================================
# PART 3 — CREATE A CLINICAL DATASET
# ============================================================

data = {
    "Patient": [
        "Ann", "James", "Sara", "David", "Mary",
        "John", "Grace", "Peter", "Lucy", "Mark"
    ],

    "Age": [
        25, 30, 35, 50, 42,
        67, 29, 54, 46, 72
    ],

    "Sex": [
        "F", "M", "F", "M", "F",
        "M", "F", "M", "F", "M"
    ],

    "Diagnosis": [
        "Hypertension",
        "Malaria",
        "Diabetes",
        "Diabetes",
        "Malaria",
        "Hypertension",
        "Malaria",
        "Diabetes",
        "Hypertension",
        "Diabetes"
    ],

    "Systolic_BP": [
        118, 125, 135, 150, 128,
        165, 110, 145, 155, 175
    ],

    "Heart_Rate": [
        72, 88, 95, 102, 80,
        110, 68, 98, 105, 115
    ],

    "Temperature": [
        36.7, 37.2, 37.8, 36.9, 38.1,
        36.8, 36.5, 37.0, 36.9, 37.3
    ],

    "Weight_kg": [
        60, 72, 68, 85, 65,
        90, 55, 82, 70, 95
    ]
}

df = pd.DataFrame(data)


# ============================================================
# PART 4 — FIRST LOOK AT THE DATA
# ============================================================

# The first EDA question is:
#
#     "What exactly am I looking at?"
#
# Display the complete dataset.

print(df)


# ============================================================
# PART 5 — UNDERSTAND DATASET SIZE
# ============================================================

# df.shape returns:
#
#     (number_of_rows, number_of_columns)
#
# Our dataset contains:
#
#     10 patients
#     8 variables

print(df.shape)


# ============================================================
# PART 6 — VIEW THE FIRST FEW ROWS
# ============================================================

# head() gives us a quick look at the beginning
# of the dataset.

print(df.head())


# ============================================================
# PART 7 — INSPECT DATA STRUCTURE
# ============================================================

# info() shows:
#
# - column names
# - number of non-null values
# - data types
# - memory usage
#
# This helps us distinguish numerical variables
# from categorical variables.

print(df.info())


# ============================================================
# PART 8 — DATA TYPES
# ============================================================

# Numerical variables in this dataset include:
#
# Age
# Systolic_BP
# Heart_Rate
# Temperature
# Weight_kg
#
# Categorical variables include:
#
# Sex
# Diagnosis
#
# Patient is an identifier.


# ============================================================
# PART 9 — CHECK FOR MISSING VALUES
# ============================================================

# Missing data can affect our analysis.
#
# isnull() identifies missing values.
#
# sum() counts them for each column.

print(df.isnull().sum())


# ============================================================
# PART 10 — CHECK FOR DUPLICATES
# ============================================================

# duplicated() identifies completely duplicated rows.
#
# sum() counts the number of duplicated rows.

print(df.duplicated().sum())


# IMPORTANT:
#
# Zero duplicated rows does NOT necessarily prove that
# no patient appears more than once.
#
# It only means that no complete rows are identical.
#
# EDA requires us to understand what one row represents.


# ============================================================
# PART 11 — DESCRIBE NUMERICAL VARIABLES
# ============================================================

# describe() provides summary statistics for
# numerical variables.
#
# It includes:
#
# - count
# - mean
# - standard deviation
# - minimum
# - 25th percentile
# - median
# - 75th percentile
# - maximum

print(df.describe())


# ============================================================
# PART 12 — EXPLORE INDIVIDUAL NUMERICAL VARIABLES
# ============================================================

# We can investigate one variable at a time.

print(df["Age"].describe())

print(df["Systolic_BP"].describe())

print(df["Heart_Rate"].describe())

print(df["Temperature"].describe())

print(df["Weight_kg"].describe())


# ============================================================
# PART 13 — EXPLORE CATEGORICAL VARIABLES
# ============================================================

# value_counts() tells us how frequently
# each category occurs.

print(df["Diagnosis"].value_counts())

print(df["Sex"].value_counts())


# ============================================================
# PART 14 — GROUP AND COMPARE
# ============================================================

# EDA becomes more useful when we compare variables
# across meaningful groups.
#
# groupby() allows us to divide the data into groups
# and calculate a summary for each group.

print(
    df.groupby("Diagnosis")["Systolic_BP"].mean()
)


# This answers:
#
#     "What is the average systolic BP within each
#      diagnosis group?"
#
# The pattern in our dataset is:
#
# Diabetes        151.25
# Hypertension    146.00
# Malaria         121.00
#
# Important:
#
# This describes an association in THIS dataset.
#
# It does not prove that diabetes causes higher BP.


# ============================================================
# PART 15 — EXPLORE DISTRIBUTIONS
# ============================================================

# A mean alone may hide important information.
#
# We therefore examine distributions.
#
# Histograms show how observations are distributed
# across ranges.

df["Age"].plot(
    kind="hist",
    bins=5
)


# We can also examine systolic BP.

df["Systolic_BP"].plot(
    kind="hist",
    bins=5
)


# When looking at distributions, investigate:
#
# - clustering
# - spread
# - skewness
# - concentration
# - gaps
# - possible multiple groups
#
# Do not focus only on which bar is tallest.


# ============================================================
# PART 16 — IDENTIFY POSSIBLE OUTLIERS
# ============================================================

# An outlier is an observation that appears unusually
# distant from the rest of the data.
#
# Example:
#
#     72
#     75
#     78
#     80
#     82
#     220
#
# The value 220 would deserve investigation.
#
# But:
#
#     OUTLIER != AUTOMATICALLY WRONG
#
# An unusual clinical measurement may be:
#
# - a genuine finding
# - measurement error
# - data-entry error
# - a special clinical circumstance
# - an unusual patient
#
# EDA identifies suspicious observations.
# Further investigation determines what they mean.


# ============================================================
# PART 17 — EXPLORE RELATIONSHIPS
# ============================================================

# EDA is not only about individual variables.
#
# We also investigate relationships between variables.
#
# Example:
#
#     Does systolic BP appear to change with age?

df.plot(
    x="Age",
    y="Systolic_BP",
    kind="scatter"
)


# Another possible relationship:
#
#     Does heart rate appear to change with systolic BP?

df.plot(
    x="Systolic_BP",
    y="Heart_Rate",
    kind="scatter"
)


# When examining scatter plots, look for:
#
# - positive association
# - negative association
# - weak association
# - strong association
# - clusters
# - unusual observations
#
# IMPORTANT:
#
# Association does not prove causation.


# ============================================================
# PART 18 — EDA THINKING
# ============================================================

# Good EDA does not stop after producing a statistic.
#
# For example:
#
#     Diabetes patients have a higher mean BP.
#
# That is an observation.
#
# The next EDA questions might be:
#
# - Are the diabetes patients older?
# - Are the diagnosis groups different in sex distribution?
# - Are there unusual BP measurements?
# - Is the sample large enough?
# - Would the pattern remain in a larger dataset?
# - Could another variable explain the difference?
#
# This is the difference between:
#
#     RUNNING ANALYSIS
#
# and:
#
#     INVESTIGATING DATA.


# ============================================================
# PART 19 — THE COMPLETE EDA WORKFLOW
# ============================================================

# A practical EDA workflow is:
#
# 1. Understand the dataset
#
# 2. Inspect structure and data types
#
# 3. Check missing values
#
# 4. Check duplicates
#
# 5. Explore numerical variables
#
# 6. Explore categorical variables
#
# 7. Examine distributions
#
# 8. Identify possible outliers and anomalies
#
# 9. Explore relationships between variables
#
# 10. Generate preliminary observations and questions
#
#
# The workflow can be remembered as:
#
#     UNDERSTAND
#          ↓
#     INSPECT
#          ↓
#     CHECK
#          ↓
#     DESCRIBE
#          ↓
#     EXPLORE
#          ↓
#     COMPARE
#          ↓
#     INVESTIGATE
#          ↓
#     QUESTION


# ============================================================
# PART 20 — CLINICAL INTERPRETATION
# ============================================================

# In healthcare data science, EDA can help us identify:
#
# - unusual clinical measurements
# - missing patient information
# - imbalanced diagnosis groups
# - possible relationships between risk factors
# - differences between patient groups
# - patterns that deserve further investigation
#
# Example:
#
# If older patients appear to have higher systolic BP,
# EDA identifies that pattern.
#
# We should then ask whether the relationship persists
# after considering other variables.
#
# EDA therefore helps generate hypotheses.
#
# It does not by itself establish causation.


# ============================================================
# PART 21 — MINI-PROJECT: CLINICAL EDA INVESTIGATION
# ============================================================

# Our clinical EDA investigation should answer:
#
# 1. How large is the dataset?
# 2. What variables are available?
# 3. What are the data types?
# 4. Are there missing values?
# 5. Are there duplicate rows?
# 6. What do the numerical variables look like?
# 7. How are diagnoses distributed?
# 8. Are there unusual measurements?
# 9. Do variables appear to be related?
# 10. Do diagnosis groups differ?
# 11. What patterns appear interesting?
# 12. What questions should be investigated next?
#
# The final output of EDA is not simply a collection
# of statistics.
#
# It is a better understanding of the dataset.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. EDA means Exploratory Data Analysis.
#
# 2. EDA is an investigation of a dataset before
#    formal statistical analysis or modelling.
#
# 3. Start by understanding what each row and column represents.
#
# 4. Inspect structure using:
#
#       df.shape
#       df.head()
#       df.info()
#
# 5. Check data quality using:
#
#       df.isnull().sum()
#       df.duplicated().sum()
#
# 6. Explore numerical variables using:
#
#       df.describe()
#
# 7. Explore categorical variables using:
#
#       df["column"].value_counts()
#
# 8. Compare groups using:
#
#       df.groupby("group")["variable"].mean()
#
# 9. Use visualizations to investigate distributions
#    and relationships.
#
# 10. An outlier is not automatically an error.
#
# 11. Association does not prove causation.
#
# 12. The most important EDA skill is learning to ask:
#
#       "What does this pattern make me want to investigate next?"
#
# ============================================================
# END OF LESSON 33
# ============================================================