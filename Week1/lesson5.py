name = input("Enter name")
age = float(input("Enter age(years)"))
Temperature = float(input("temperature(°C)"))
heart_rate = int(input("Enter heart rate"))
weight = float(input("Enter weight(kg)"))
height = float(input("Enter height(meters)"))
bmi = round(weight / (height * height), 1)
print()
print()

print("=======================")
print("  PATIENT TRIAGE TOOL")
print("=======================")


print()
print()



print("--------")
print("BIODATA")
print("--------")
print()

print("Patient name:", name)
print("Patient age:", int(age), "years")


print("------------")
print("VITAL SIGNS")
print("------------")
print()

print("Temperature")
print("------------")
print("Temperature:", Temperature, "°C")
if Temperature < 35:
    print("Assessment:", "Hypothermia")
elif Temperature >= 38:
    print("Assessment:", "Fever")
else:
    print("Assessment:", "Normal")

print()        

print("Heart rate")
print("-----------")
print("Heart rate:", heart_rate, "bpm")
if heart_rate < 60:
    print( "Assessment:", "Bradycardia")
elif heart_rate > 100:
    print("Assessment", "Tachycardia")
else:
    print("Assessment:", "Normal")
    print()
    print()


print("----------------")
print("ANTHROPOMETRICS")
print("----------------")
print("Weight:", weight, "kgs")
print("Height:", height,"m")
print()

print("BMI:", bmi)
if bmi < 18.5:
    print("Assessment:", "underweight")
elif bmi < 25:
    print("Assessment:", "healthy weight")
elif bmi < 30:
    print("Assessment", "overweight")
else:
    print("Assessment", "obesity")
