# Project Phoenix – Python Cheat Sheet

> **Purpose:** A quick reference for Python syntax learned in Lessons 1–8.

---

# Variables

```python
name = "John"          # String
age = 30               # Integer
temperature = 37.2     # Float
```

---

# Printing

```python
print(name)
print(age)
print("Age:", age)
```

---

# User Input

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter weight: "))
```

---

# Type Conversion

```python
int()
float()
str()
```

Examples

```python
age = int("25")
weight = float("70.5")
number = str(100)
```

---

# Arithmetic Operators

```python
+
-
*
/
/
//
%
**
```

Example

```python
total = a + b
bmi = weight / (height ** 2)
```

---

# Comparison Operators

```python
==
!=
>
<
>=
<=
```

Example

```python
if age >= 18:
    print("Adult")
```

---

# Logical Operators

```python
and
or
not
```

Example

```python
if age > 60 and temperature > 38:
    print("Urgent review")
```

---

# if Statements

```python
if condition:
    ...

elif condition:
    ...

else:
    ...
```

---

# Nested if

```python
if age >= 18:
    if pregnant == "yes":
        print("Refer to ANC")
```

---

# while Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# for Loop

```python
for number in range(5):
    print(number)
```

With start and stop

```python
for number in range(1, 6):
    print(number)
```

With step

```python
for number in range(0, 11, 2):
    print(number)
```

Loop through a list

```python
for patient in patients:
    print(patient)
```

---

# Lists

Create

```python
patients = ["John", "Mary", "David"]
```

Access items

```python
patients[0]
patients[1]
patients[-1]
```

Modify items

```python
patients[1] = "Maria"
```

---

# List Methods

Add item

```python
patients.append("Grace")
```

Remove by value

```python
patients.remove("Grace")
```

Remove by index

```python
patients.pop(0)
```

Length

```python
len(patients)
```

Sort

```python
patients.sort()
```

Reverse

```python
patients.reverse()
```

Count occurrences

```python
patients.count("John")
```

Find index

```python
patients.index("John")
```

---

# Useful Patterns

Print every patient

```python
for patient in patients:
    print(patient)
```

Display total patients

```python
print("Total Patients:", len(patients))
```

Add then remove

```python
patients.append("Grace")
patients.remove("Chris")
```

---

# Common Beginner Mistakes

❌

```python
Patients.append("John")
```

✅

```python
patients.append("John")
```

---

❌

```python
print("patient")
```

✅

```python
print(patient)
```

---

❌

```python
patients.len()
```

✅

```python
len(patients)
```

---

❌

```python
patient[0]
```

when the variable is

```python
patients = [...]
```

✅

```python
patients[0]
```

---

# Project Phoenix Rule

**Predict the output before running the code.**

Think first.
Code second.
Run third.
Debug last.
