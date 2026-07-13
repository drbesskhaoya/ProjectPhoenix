# Project Phoenix Handbook

## Week 1 – Python Fundamentals

# Lesson 7 – `for` Loops

## Objective

By the end of this lesson you should be able to:

* Understand what a `for` loop is.
* Explain the difference between `for` and `while` loops.
* Use the `range()` function.
* Count forwards and backwards.
* Use the `step` value in `range()`.
* Write nested `for` loops.
* Solve simple programming problems using `for` loops.

---

# What is a `for` Loop?

A `for` loop repeats a block of code a fixed number of times.

Unlike a `while` loop, Python automatically keeps track of the loop variable, making `for` loops easier and less prone to mistakes.

Example:

```python
for number in range(5):
    print(number)
```

Output:

```
0
1
2
3
4
```

---

# The `range()` Function

`range()` generates a sequence of numbers.

## 1. `range(stop)`

```python
for number in range(5):
    print(number)
```

Output:

```
0
1
2
3
4
```

Python starts at **0** and stops **before** the stop value.

---

## 2. `range(start, stop)`

```python
for number in range(1, 6):
    print(number)
```

Output:

```
1
2
3
4
5
```

Python starts at **1** and stops before **6**.

---

## 3. `range(start, stop, step)`

```python
for number in range(0, 11, 2):
    print(number)
```

Output:

```
0
2
4
6
8
10
```

Python increases by **2** each time.

---

# Counting Backwards

A negative step allows Python to count backwards.

```python
for number in range(10, 0, -1):
    print(number)
```

Output:

```
10
9
8
7
6
5
4
3
2
1
```

---

# `for` vs `while`

Use a **for loop** when you know how many times something should repeat.

Example:

```python
for patient in range(1, 6):
    print("Checking Patient", patient)
```

Use a **while loop** when repetition depends on a condition.

Example:

```python
temperature = 39

while temperature > 37.5:
    print("Patient still has a fever.")
    temperature -= 0.5
```

---

# Nested `for` Loops

A nested loop is simply a loop inside another loop.

Example:

```python
for room in range(1, 4):
    for bed in range(1, 3):
        print("Room", room, "- Bed", bed)
```

Output:

```
Room 1 - Bed 1
Room 1 - Bed 2
Room 2 - Bed 1
Room 2 - Bed 2
Room 3 - Bed 1
Room 3 - Bed 2
```

Nested loops are useful when working with rows and columns, rooms and beds, doctors and patients, or any situation involving two repeating groups.

---

# Medical Example 1 – Patient List

```python
for patient in range(1, 6):
    print("Patient", patient)
```

Output:

```
Patient 1
Patient 2
Patient 3
Patient 4
Patient 5
```

---

# Medical Example 2 – Multiplication Table

```python
for number in range(1, 6):
    print(number, "x 2 =", number * 2)
```

Output:

```
1 x 2 = 2
2 x 2 = 4
3 x 2 = 6
4 x 2 = 8
5 x 2 = 10
```

---

# Mini Project – Patient Observation Logger

```python
for patient in range(1, 6):
    print("Patient", patient)
    print("Temperature checked")
    print("Pulse checked")
    print("Observation complete")
    print()
```

Output:

```
Patient 1
Temperature checked
Pulse checked
Observation complete

Patient 2
Temperature checked
Pulse checked
Observation complete

Patient 3
Temperature checked
Pulse checked
Observation complete

Patient 4
Temperature checked
Pulse checked
Observation complete

Patient 5
Temperature checked
Pulse checked
Observation complete
```

---

# Key Points

* `for` loops repeat code a fixed number of times.
* `range(stop)` starts at **0**.
* `range(start, stop)` starts at the specified number.
* The **stop value is never included**.
* `range(start, stop, step)` allows counting by different intervals.
* A negative step counts backwards.
* Use `for` when the number of repetitions is known.
* Use `while` when repetition depends on a condition.
* Nested loops repeat one loop inside another.

---


**Status:** ✅ Lesson 7 Complete
