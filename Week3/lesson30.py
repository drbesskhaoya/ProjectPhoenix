# PROJECT PHOENIX
# Lesson 30 — Pandas Analysis

import pandas as pd


# ============================================================
# 1. CREATE THE DATASET
# ============================================================

data = {
    "Patient": [
        "Ann", "James", "Sara", "David",
        "Mary", "Peter", "Lucy"
    ],
    "Age": [25, 30, 35, 50, 42, 29, 61],
    "Diagnosis": [
        "Hypertension",
        "Malaria",
        "Leukemia",
        "Diabetes",
        "Malaria",
        "Hypertension",
        "Diabetes"
    ]
}

df = pd.DataFrame(data)


# ============================================================
# 2. BASIC STATISTICAL ANALYSIS
# ============================================================

print("AVERAGE AGE:")
print(df["Age"].mean())

print("\nMEDIAN AGE:")
print(df["Age"].median())

print("\nYOUNGEST PATIENT:")
print(df["Age"].min())

print("\nOLDEST PATIENT:")
print(df["Age"].max())

print("\nTOTAL AGE:")
print(df["Age"].sum())

print("\nNUMBER OF PATIENTS:")
print(df["Age"].count())


# ============================================================
# 3. DIAGNOSIS FREQUENCY
# ============================================================

print("\nPATIENTS BY DIAGNOSIS:")
print(df["Diagnosis"].value_counts())


# ============================================================
# 4. GROUPBY — AVERAGE AGE BY DIAGNOSIS
# ============================================================

print("\nAVERAGE AGE BY DIAGNOSIS:")
print(df.groupby("Diagnosis")["Age"].mean())


# ============================================================
# 5. GROUPBY — MULTIPLE STATISTICS
# ============================================================

print("\nAGE SUMMARY BY DIAGNOSIS:")

age_summary = df.groupby("Diagnosis")["Age"].agg(
    ["mean", "min", "max", "count"]
)

print(age_summary)


# ============================================================
# KEY TAKEAWAY
# ============================================================

# Pandas allows us to transform raw data into
# meaningful summaries and identify patterns
# within different groups of patients.