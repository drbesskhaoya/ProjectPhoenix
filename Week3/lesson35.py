import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# PROJECT PHOENIX — FIRST MAJOR HEALTHCARE DATA SCIENCE PROJECT
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 1. CREATE SYNTHETIC HEALTHCARE DATA
# ------------------------------------------------------------

np.random.seed(42)

n_patients = 100

data = {
    "Patient_ID": range(1, n_patients + 1),

    "Age": np.random.randint(20, 81, n_patients),

    "Sex": np.random.choice(
        ["Female", "Male"],
        n_patients
    ),

    "BMI": np.round(
        np.random.normal(27, 5, n_patients),
        1
    ),

    "Systolic_BP": np.random.randint(
        100, 181, n_patients
    ),

    "Diastolic_BP": np.random.randint(
        60, 111, n_patients
    ),

    "Glucose": np.random.randint(
        70, 201, n_patients
    ),

    "Cholesterol": np.random.randint(
        130, 281, n_patients
    ),

    "Diagnosis": np.random.choice(
        [
            "Hypertension",
            "Diabetes",
            "Malaria",
            "Healthy"
        ],
        n_patients
    ),

    "Smoking": np.random.choice(
        ["Yes", "No"],
        n_patients
    ),

    "Hospital_Days": np.random.randint(
        1, 15, n_patients
    )
}

df = pd.DataFrame(data)

print(df.head())


# ------------------------------------------------------------
# 2. DATA VALIDATION
# ------------------------------------------------------------

print("\nDataset shape:")
print(df.shape)

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nSummary statistics:")
print(df.describe())

# ------------------------------------------------------------
# 3. CREATE CLINICAL RISK FLAGS
# ------------------------------------------------------------

df["High_BP"] = df["Systolic_BP"] >= 140

df["High_Glucose"] = df["Glucose"] >= 126

df["High_Cholesterol"] = df["Cholesterol"] >= 200

df["High_BMI"] = df["BMI"] >= 25

print("\nClinical risk flags:")
print(df[
    [
        "Patient_ID",
        "Systolic_BP",
        "Glucose",
        "Cholesterol",
        "BMI",
        "High_BP",
        "High_Glucose",
        "High_Cholesterol",
        "High_BMI"
    ]
].head())

# ------------------------------------------------------------
# 4. RISK FACTOR PREVALENCE
# ------------------------------------------------------------

risk_factors = [
    "High_BP",
    "High_Glucose",
    "High_Cholesterol",
    "High_BMI"
]

risk_prevalence = df[risk_factors].mean() * 100

print("\nRisk factor prevalence (%):")
print(risk_prevalence.round(1))

# ------------------------------------------------------------
# 5. RISK FACTORS BY DIAGNOSIS
# ------------------------------------------------------------

risk_by_diagnosis = (
    df.groupby("Diagnosis")[risk_factors]
      .mean()
      .mul(100)
      .round(1)
)

print("\nRisk factor prevalence by diagnosis (%):")
print(risk_by_diagnosis)

# ------------------------------------------------------------
# 6. DIAGNOSIS DISTRIBUTION
# ------------------------------------------------------------

diagnosis_counts = df["Diagnosis"].value_counts()

print("\nPatients by diagnosis:")
print(diagnosis_counts)
# ------------------------------------------------------------
# 7. HOSPITAL LENGTH OF STAY BY DIAGNOSIS
# ------------------------------------------------------------

length_of_stay = (
    df.groupby("Diagnosis")["Hospital_Days"]
      .agg(["mean", "median", "min", "max", "count"])
      .round(1)
)

print("\nHospital length of stay by diagnosis:")
print(length_of_stay)

# ------------------------------------------------------------
# 8. COMPOSITE RISK SCORE
# ------------------------------------------------------------

df["Risk_Score"] = df[risk_factors].sum(axis=1)

print("\nRisk score distribution:")
print(df["Risk_Score"].value_counts().sort_index())

# ------------------------------------------------------------
# 9. RISK SCORE AND HOSPITAL LENGTH OF STAY
# ------------------------------------------------------------

stay_by_risk = (
    df.groupby("Risk_Score")["Hospital_Days"]
      .agg(["mean", "median", "count"])
      .round(1)
)

print("\nHospital stay by risk score:")
print(stay_by_risk)

# ------------------------------------------------------------
# 10. RISK SCORE VS HOSPITAL STAY
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Risk_Score"],
    df["Hospital_Days"],
    alpha=0.7
)

plt.xlabel("Risk Score")
plt.ylabel("Hospital Days")
plt.title("Risk Score vs Hospital Length of Stay")

plt.grid(True)
plt.show()
# ------------------------------------------------------------
# 11. CORRELATION
# ------------------------------------------------------------

correlation = df["Risk_Score"].corr(df["Hospital_Days"])

print("\nCorrelation between risk score and hospital stay:")
print(round(correlation, 3))
# ------------------------------------------------------------
# 12. IDENTIFY PATIENTS WITH HIGH RISK BURDEN
# ------------------------------------------------------------

high_risk_patients = df[df["Risk_Score"] >= 3]

print("\nPatients with 3 or more risk factors:")
print(
    high_risk_patients[
        [
            "Patient_ID",
            "Age",
            "Sex",
            "Diagnosis",
            "BMI",
            "Systolic_BP",
            "Glucose",
            "Cholesterol",
            "Risk_Score",
            "Hospital_Days"
        ]
    ].sort_values(
        "Risk_Score",
        ascending=False
    )
)

# ------------------------------------------------------------
# 13. FINAL PROJECT SUMMARY
# ------------------------------------------------------------

summary = pd.DataFrame({
    "Metric": [
        "Total patients",
        "Mean age",
        "Mean BMI",
        "Mean systolic BP",
        "Mean glucose",
        "Mean cholesterol",
        "Mean hospital stay",
        "High BP prevalence",
        "High glucose prevalence",
        "High cholesterol prevalence",
        "High BMI prevalence",
        "Patients with 3+ risk factors",
        "Risk score vs hospital stay correlation"
    ],

    "Value": [
        len(df),
        round(df["Age"].mean(), 1),
        round(df["BMI"].mean(), 1),
        round(df["Systolic_BP"].mean(), 1),
        round(df["Glucose"].mean(), 1),
        round(df["Cholesterol"].mean(), 1),
        round(df["Hospital_Days"].mean(), 1),
        round(df["High_BP"].mean() * 100, 1),
        round(df["High_Glucose"].mean() * 100, 1),
        round(df["High_Cholesterol"].mean() * 100, 1),
        round(df["High_BMI"].mean() * 100, 1),
        round((df["Risk_Score"] >= 3).mean() * 100, 1),
        round(correlation, 3)
    ]
})

print("\nFINAL PROJECT SUMMARY")
print(summary.to_string(index=False))

# ------------------------------------------------------------
# 14. VISUALIZE HOSPITAL STAY BY DIAGNOSIS
# ------------------------------------------------------------

mean_stay = (
    df.groupby("Diagnosis")["Hospital_Days"]
      .mean()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

mean_stay.plot(kind="bar")

plt.xlabel("Diagnosis")
plt.ylabel("Mean Hospital Stay (days)")
plt.title("Mean Hospital Stay by Diagnosis")

plt.xticks(rotation=0)
plt.grid(axis="y")
plt.tight_layout()
plt.show()