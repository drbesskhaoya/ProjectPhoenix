# Project Phoenix 

# Lesson 8 – Lists

## Learning Objectives


* Understand what a list is
* Create lists
* Access list items using indexes
* Use positive and negative indexing
* Modify list items
* Add new items to a list
* Remove items from a list
* Loop through lists using a `for` loop
* Use common list methods
* Build a simple Patient Management System

---

# What is a List?

A **list** is a collection of multiple values stored in a single variable.

Instead of creating many variables:

```python
patient1 = "John"
patient2 = "Mary"
patient3 = "David"
```

We can store everything in one list:

```python
patients = ["John", "Mary", "David"]
```

Lists use **square brackets `[]`** and items are separated by commas.

Lists can contain:

### Strings

```python
patients = ["John", "Mary", "David"]
```

### Numbers

```python
temperatures = [36.5, 37.2, 38.8]
```

### Mixed Data Types

```python
patient = ["John", 35, 37.2]
```

Although Python allows mixed data types, it is good practice to keep similar data together.

---

# Printing a List

```python
patients = ["John", "Mary", "David"]

print(patients)
```

Output

```text
['John', 'Mary', 'David']
```

Python prints the entire list with brackets, commas and quotation marks.

---

# Accessing List Items (Indexing)

Each item has an index.

```text
Index      0      1      2      3      4
Patient   John   Mary   David   Sarah   Grace
```

Example:

```python
patients = ["John", "Mary", "David", "Sarah", "Grace"]

print(patients[0])
```

Output

```text
John
```

---

# Negative Indexing

Python can count from the end of the list.

```text
Index

-1  Grace
-2  Sarah
-3  David
-4  Mary
-5  John
```

Example

```python
patients = ["John", "Mary", "David", "Sarah", "Grace"]

print(patients[-1])
```

Output

```text
Grace
```

---

# Modifying List Items

Items can be changed using their index.

```python
patients = ["John", "Mary", "David"]

patients[1] = "Maria"

print(patients)
```

Output

```text
['John', 'Maria', 'David']
```

---

# Adding Items

Use `append()` to add an item to the end of the list.

```python
patients = ["John", "Maria"]

patients.append("Grace")

print(patients)
```

Output

```text
['John', 'Maria', 'Grace']
```

---

# Removing Items

## remove()

Removes an item by its value.

```python
patients = ["John", "Maria", "Grace"]

patients.remove("Maria")

print(patients)
```

Output

```text
['John', 'Grace']
```

---

## pop()

Removes an item by its index.

```python
patients = ["John", "Maria", "Grace"]

patients.pop(0)

print(patients)
```

Output

```text
['Maria', 'Grace']
```

`pop()` also returns the item that was removed.

Example

```python
patients = ["John", "Maria", "Grace"]

removed_patient = patients.pop(0)

print(removed_patient)
print(patients)
```

Output

```text
John
['Maria', 'Grace']
```

---

# Looping Through a List

Use a `for` loop to process every item.

```python
patients = ["John", "Maria", "Grace"]

for patient in patients:
    print(patient)
```

Output

```text
John
Maria
Grace
```

Medical example

```python
temperatures = [36.5, 37.2, 38.8, 39.1]

for temperature in temperatures:
    print("Temperature:", temperature)
```

Output

```text
Temperature: 36.5
Temperature: 37.2
Temperature: 38.8
Temperature: 39.1
```

---

# Useful List Methods

## len()

Returns the number of items.

```python
patients = ["John", "Maria", "Daniel"]

print(len(patients))
```

Output

```text
3
```

---

## sort()

Sorts a list into ascending order.

```python
patients = ["Grace", "John", "Daniel", "Maria"]

patients.sort()

print(patients)
```

Output

```text
['Daniel', 'Grace', 'John', 'Maria']
```

---

## reverse()

Reverses the current order of a list.

```python
patients = ["John", "Maria", "Daniel"]

patients.reverse()

print(patients)
```

Output

```text
['Daniel', 'Maria', 'John']
```

---

## count()

Counts how many times an item appears.

```python
patients = ["John", "Maria", "John", "Grace", "John"]

print(patients.count("John"))
```

Output

```text
3
```

---

## index()

Returns the index of the first occurrence of an item.

```python
patients = ["John", "Maria", "Grace"]

print(patients.index("Grace"))
```

Output

```text
2
```

---

# Summary Table

| Method      | Purpose                   |
| ----------- | ------------------------- |
| `append()`  | Add an item to the end    |
| `remove()`  | Remove by value           |
| `pop()`     | Remove by index           |
| `len()`     | Count items               |
| `sort()`    | Sort the list             |
| `reverse()` | Reverse the order         |
| `count()`   | Count occurrences         |
| `index()`   | Find the index of an item |

---

# Mini Project – Patient Management System

```python
patients = ["Alex", "Brandon", "Kate", "Chris"]

print("Current Patients:")
for patient in patients:
    print(patient)

patients.append("Grace")

patients.remove("Chris")

print("\nTotal Patients:", len(patients))

print("\nUpdated Patients:")
for patient in patients:
    print(patient)
```

Output

```text
Current Patients:
Alex
Brandon
Kate
Chris

Total Patients: 4

Updated Patients:
Alex
Brandon
Kate
Grace
```

---

# Key Takeaways

* Lists store multiple values in one variable.
* Python indexes begin at **0**.
* Negative indexes count from the end of the list.
* Use `append()` to add items.
* Use `remove()` to remove an item by value.
* Use `pop()` to remove an item by index.
* Use `len()` to count the number of items.
* Use `sort()` to arrange items in ascending order.
* Use `reverse()` to reverse the order of a list.
* Use `count()` to count occurrences of a value.
* Use `index()` to find the position of a value.
* `for` loops make it easy to process every item in a list.

---

# Lesson 8 Complete ✅

