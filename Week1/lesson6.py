# ============================================
# PROJECT PHOENIX
# Day 6 - While Loops Practice
# ============================================

# --------------------------------------------
# Example 1: Count from 1 to 5
# --------------------------------------------

count = 1

while count <= 5:
    print(count)
    count += 1

print()


# --------------------------------------------
# Example 2: Countdown
# --------------------------------------------

count = 5

while count >= 1:
    print(count)
    count -= 1

print("Blast off!")

print()


# --------------------------------------------
# Example 3: Even numbers
# --------------------------------------------

count = 2

while count <= 20:
    print(count)
    count += 2

print()


# --------------------------------------------
# Example 4: Password Checker
# --------------------------------------------

password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access Granted")

print()


# --------------------------------------------
# Exercise 1: Blood Pressure Recorder
# --------------------------------------------

print("BLOOD PRESSURE")
print("----------------")

blood_pressure = int(input("Enter systolic BP: "))

while blood_pressure > 0:

    if blood_pressure < 90:
        print("Low")

    elif blood_pressure <= 120:
        print("Normal")

    else:
        print("High")

    blood_pressure = int(input("Enter systolic BP: "))

print("Blood pressure recording ended.")

print()


# --------------------------------------------
# Exercise 2: BMI Category
# --------------------------------------------

print("BMI")
print("----")

bmi = float(input("Enter BMI: "))

while bmi > 0:

    if bmi < 18.5:
        print("Underweight")

    elif bmi <= 24.9:
        print("Normal")

    elif bmi <= 29.9:
        print("Overweight")

    else:
        print("Obese")

    bmi = float(input("Enter BMI: "))

print("BMI recording ended.")

print()


# --------------------------------------------
# Exercise 3: Heart Rate Monitor
# --------------------------------------------

print("HEART RATE")
print("-----------")

heart_rate = int(input("Enter heart rate: "))

while heart_rate > 0:

    if heart_rate >= 60 and heart_rate <= 100:
        print("Heart rate:", heart_rate, "(Normal)")
    else:
        print("Heart rate:", heart_rate, "(Abnormal)")

    heart_rate = int(input("Enter heart rate: "))

print("Heart rate recording ended.")




    




     
