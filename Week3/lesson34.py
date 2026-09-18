# ============================================================
# PROJECT PHOENIX
# LESSON 34 — STATISTICS FOR HEALTHCARE DATA SCIENCE
# ============================================================
#
# Topics:
# 1. Mean, Median, and Mode
# 2. Range
# 3. Variance
# 4. Standard Deviation
# 5. Percentiles and Quartiles
# 6. Interquartile Range (IQR)
# 7. Z-Scores
# 8. Correlation
# 9. Statistical Significance
# 10. Healthcare Statistics Mini-Project
#
# ============================================================


# ============================================================
# PART 1 — IMPORTS
# ============================================================

import statistics
import numpy as np
import pandas as pd


# ============================================================
# PART 2 — MEAN, MEDIAN, AND MODE
# ============================================================

ages = [25, 30, 35, 40, 50]

mean_age = statistics.mean(ages)
median_age = statistics.median(ages)

print("Mean:", mean_age)
print("Median:", median_age)


# Mode example

diagnoses = [
    "Hypertension",
    "Diabetes",
    "Hypertension",
    "Malaria",
    "Hypertension"
]

mode_diagnosis = statistics.mode(diagnoses)

print("Mode:", mode_diagnosis)


# ============================================================
# PART 3 — MEAN VS MEDIAN
# ============================================================
#
# Extreme values can affect the mean.
# The median is often more resistant to extreme values.
#
# Example:
#
# 20, 22, 24, 25, 27, 29, 90
#
# The value 90 pulls the mean upward,
# while the median remains closer to the center.
#
# ============================================================


ages_with_outlier = [20, 22, 24, 25, 27, 29, 90]

print("\nData with an extreme value:")
print("Mean:", statistics.mean(ages_with_outlier))
print("Median:", statistics.median(ages_with_outlier))


# ============================================================
# PART 4 — RANGE
# ============================================================
#
# Range = Maximum - Minimum
#
# ============================================================

systolic_bp = [
    118, 125, 130, 135, 142,
    150, 160, 128, 132, 145
]

bp_range = max(systolic_bp) - min(systolic_bp)

print("\nBlood Pressure Range:")
print(bp_range)


# ============================================================
# PART 5 — VARIANCE
# ============================================================
#
# Variance measures how spread out observations are
# around the mean.
#
# Higher variance = greater spread
# Lower variance = observations closer together
#
# ============================================================

variance_bp = statistics.variance(systolic_bp)

print("\nBlood Pressure Variance:")
print(variance_bp)


# ============================================================
# PART 6 — STANDARD DEVIATION
# ============================================================
#
# Standard deviation measures the spread of observations
# around the mean.
#
# Small SD = values are relatively clustered
# Large SD = values are more widely spread
#
# ============================================================

std_bp = statistics.stdev(systolic_bp)

print("\nBlood Pressure Standard Deviation:")
print(std_bp)


# ============================================================
# PART 7 — PERCENTILES AND QUARTILES
# ============================================================
#
# Percentiles describe the position of values within
# a distribution.
#
# 25th percentile = Q1
# 50th percentile = Q2 = Median
# 75th percentile = Q3
#
# ============================================================

q1 = np.percentile(systolic_bp, 25)
q2 = np.percentile(systolic_bp, 50)
q3 = np.percentile(systolic_bp, 75)

print("\nBlood Pressure Quartiles:")
print("Q1:", q1)
print("Q2 / Median:", q2)
print("Q3:", q3)


# ============================================================
# PART 8 — INTERQUARTILE RANGE (IQR)
# ============================================================
#
# IQR = Q3 - Q1
#
# IQR represents the spread of the middle 50%
# of observations.
#
# IQR is less affected by extreme values than the range.
#
# ============================================================

iqr = q3 - q1

print("\nBlood Pressure IQR:")
print(iqr)


# ============================================================
# PART 9 — Z-SCORES
# ============================================================
#
# A z-score tells us how many standard deviations an
# observation is above or below the mean.
#
# Formula:
#
# z = (x - mean) / standard deviation
#
# Positive z-score = above the mean
# Negative z-score = below the mean
#
# ============================================================

mean_bp = statistics.mean(systolic_bp)
std_bp = statistics.stdev(systolic_bp)

patient_bp = 150

z_score = (patient_bp - mean_bp) / std_bp

print("\nZ-Score:")
print(z_score)


# ============================================================
# PART 10 — CORRELATION
# ============================================================
#
# Correlation measures the strength and direction
# of a linear relationship between two variables.
#
# Correlation coefficient:
#
# -1 → +1
#
# Positive correlation:
# As one variable increases, the other tends to increase.
#
# Negative correlation:
# As one variable increases, the other tends to decrease.
#
# Near zero:
# Little or no linear relationship.
#
# IMPORTANT:
#
# Correlation does NOT prove causation.
#
# ============================================================


# ============================================================
# PART 11 — HEALTHCARE DATASET
# ============================================================

data = {
    "Patient": [
        "Ann", "James", "Sara", "David", "Mary",
        "John", "Grace", "Peter", "Lucy", "Brian"
    ],

    "Age": [
        25, 30, 35, 50, 42,
        61, 29, 55, 38, 47
    ],

    "Systolic_BP": [
        118, 125, 130, 135, 142,
        150, 160, 128, 132, 145
    ],

    "Glucose": [
        90, 110, 125, 140, 130,
        155, 100, 145, 115, 135
    ]
}

df = pd.DataFrame(data)

print("\n" + "=" * 60)
print("HEALTHCARE DATASET")
print("=" * 60)

print(df)


# ============================================================
# PART 12 — AGE STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("AGE STATISTICS")
print("=" * 60)

age_mean = df["Age"].mean()
age_median = df["Age"].median()
age_std = df["Age"].std()

print("Mean:", age_mean)
print("Median:", age_median)
print("Standard deviation:", age_std)


# ============================================================
# PART 13 — BLOOD PRESSURE STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("SYSTOLIC BLOOD PRESSURE STATISTICS")
print("=" * 60)

bp_mean = df["Systolic_BP"].mean()
bp_median = df["Systolic_BP"].median()
bp_std = df["Systolic_BP"].std()
bp_min = df["Systolic_BP"].min()
bp_max = df["Systolic_BP"].max()

print("Mean:", bp_mean)
print("Median:", bp_median)
print("Standard deviation:", bp_std)
print("Minimum:", bp_min)
print("Maximum:", bp_max)
print("Range:", bp_max - bp_min)


# ============================================================
# PART 14 — BLOOD PRESSURE QUARTILES AND IQR
# ============================================================

print("\n" + "=" * 60)
print("SYSTOLIC BLOOD PRESSURE QUARTILES")
print("=" * 60)

q1 = np.percentile(df["Systolic_BP"], 25)
q3 = np.percentile(df["Systolic_BP"], 75)

iqr = q3 - q1

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)


# ============================================================
# PART 15 — AGE VS SYSTOLIC BP CORRELATION
# ============================================================

print("\n" + "=" * 60)
print("CORRELATION")
print("=" * 60)

age_bp_correlation = df["Age"].corr(df["Systolic_BP"])

print("Age vs Systolic BP:", age_bp_correlation)


# ============================================================
# PART 16 — CORRELATION MATRIX
# ============================================================
#
# A correlation matrix allows us to examine relationships
# between multiple numerical variables.
#
# ============================================================

print("\n" + "=" * 60)
print("CORRELATION MATRIX")
print("=" * 60)

correlation_matrix = df.corr(numeric_only=True)

print(correlation_matrix)


# ============================================================
# PART 17 — STATISTICAL SIGNIFICANCE
# ============================================================
#
# In healthcare research, we often want to determine
# whether an observed difference could reasonably have
# occurred by chance under a specified statistical model.
#
# This is where hypothesis testing and p-values are used.
#
# A commonly used threshold is:
#
# p < 0.05
#
# However:
#
# Statistical significance does NOT automatically mean
# clinical importance.
#
# A result with p < 0.05 should be interpreted together
# with effect size, confidence intervals, study design,
# sample size, and clinical relevance.
#
# ============================================================


# ============================================================
# PART 18 — KEY STATISTICAL CONCEPTS
# ============================================================
#
# Mean:
# Arithmetic average.
#
# Median:
# Middle value after sorting observations.
#
# Mode:
# Most frequently occurring value.
#
# Range:
# Maximum - Minimum.
#
# Variance:
# Measure of variability around the mean.
#
# Standard deviation:
# Measure of the spread of observations around the mean.
#
# Percentile:
# Indicates the position of an observation within a dataset.
#
# Quartiles:
# Q1 = 25th percentile
# Q2 = 50th percentile
# Q3 = 75th percentile
#
# IQR:
# Q3 - Q1
#
# Z-score:
# Number of standard deviations an observation is from
# the mean.
#
# Correlation:
# Measures the strength and direction of a linear
# relationship between two variables.
#
# Correlation does NOT prove causation.
#
# P-value:
# Used in hypothesis testing to assess how compatible
# observed data are with a specified null hypothesis.
#
# ============================================================


# ============================================================
# PART 19 — HEALTHCARE DATA SCIENCE INTERPRETATION
# ============================================================
#
# Statistics should not stop at calculating numbers.
#
# The data scientist must:
#
# 1. Calculate
# 2. Examine
# 3. Interpret
# 4. Communicate
#
# Example:
#
# Mean systolic BP tells us about the average BP.
#
# Median systolic BP tells us about the central observation.
#
# Standard deviation tells us about variability.
#
# IQR tells us about the spread of the middle 50%.
#
# Correlation tells us whether two variables have a
# linear relationship.
#
# These statistics describe the dataset.
#
# They do NOT automatically establish causation or prove
# that the findings apply to a larger population.
#
# ============================================================


# ============================================================
# END OF LESSON 34
# ============================================================
#
# 
# NEXT:
#
# 35 → FIRST MAJOR HEALTHCARE DATA
#      SCIENCE PROJECT
#
# ============================================================