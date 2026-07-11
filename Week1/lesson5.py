# ==========================================================
# Lesson 5 - Decision Making (if, elif, else)
#
# Mini Project:
# Patient Triage Tool
# ==========================================================


# ==========================================================
# PATIENT INFORMATION
# ==========================================================

name = input("Enter patient name: ")
age = int(input("Enter age (years): "))
temperature = float(input("Enter temperature (°C): "))
heart_rate = int(input("Enter heart rate (bpm): "))
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

# Calculate BMI
bmi = round(weight / (height * height), 1)


# ==========================================================
# PATIENT TRIAGE REPORT
# ==========================================================

print()
print("=" * 35)
print("        PATIENT TRIAGE TOOL")
print("=" * 35)


# ==========================================================
# BIODATA
# ==========================================================

print()
print("BIODATA")
print("-" * 35)

print("Patient Name :", name)
print("Age          :", age, "years")


# ==========================================================
# VITAL SIGNS
# ==========================================================

print()
print("VITAL SIGNS")
print("-" * 35)

# ---------- Temperature ----------

print("Temperature :", temperature, "°C")

if temperature < 35:
    print("Assessment : Hypothermia")

elif temperature >= 38:
    print("Assessment : Fever")

else:
    print("Assessment : Normal")

print()

# ---------- Heart Rate ----------

print("Heart Rate  :", heart_rate, "bpm")

if heart_rate < 60:
    print("Assessment : Bradycardia")

elif heart_rate > 100:
    print("Assessment : Tachycardia")

else:
    print("Assessment : Normal")


# ==========================================================
# ANTHROPOMETRICS
# ==========================================================

print()
print("ANTHROPOMETRICS")
print("-" * 35)

print("Weight :", weight, "kg")
print("Height :", height, "m")
print("BMI    :", bmi)

if bmi < 18.5:
    print("Assessment : Underweight")

elif bmi < 25:
    print("Assessment : Healthy Weight")

elif bmi < 30:
    print("Assessment : Overweight")

else:
    print("Assessment : Obesity")


# ==========================================================
# END OF REPORT
# ==========================================================

print()
print("=" * 35)
print("Assessment Complete")
print("=" * 35)