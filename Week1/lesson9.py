# Project Phoenix 

# Lesson 9 – Functions & Variable Scope

## Learning Objectives


* Create functions
* Call functions
* Use parameters
* Return values from functions
* Understand the difference between `print()` and `return`
* Build reusable functions
* Understand local and global variables
* Modify global variables using the `global` keyword

---

# 1. Creating Functions

A function is a reusable block of code that performs a specific task.

## Syntax

```python
def function_name():
    print("Hello")
```

## Example

```python
def welcome():
    print("Welcome to Avenue Hospital")

welcome()
```

**Output**

```
Welcome to Avenue Hospital
```

---

# 2. Calling Functions

A function does not run when it is created.

It only runs when it is called.

Example:

```python
def greet():
    print("Good morning!")

greet()
```

---

# 3. Parameters

Parameters allow information to be passed into a function.

Example:

```python
def greet(patient):
    print("Hello", patient)

greet("John")
```

**Output**

```
Hello John
```

---

# 4. Return Values

A function can send a value back to the program using the `return` keyword.

Example:

```python
def square(number):
    return number * number

answer = square(4)

print(answer)
```

**Output**

```
16
```

---

# 5. print() vs return

## print()

Displays information on the screen.

```python
def hello():
    print("Hello")
```

Use `print()` when you simply want to display information.

---

## return

Returns a value back to the program.

```python
def add(a, b):
    return a + b

result = add(3, 5)

print(result)
```

Use `return` when another part of the program needs to use the value.

---

# 6. BMI Function

Example:

```python
def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

result = calculate_bmi(70, 1.75)

print(result)
```

---

# 7. Variable Scope

A variable's **scope** is where it can be accessed in a program.

There are two main types:

* Local variables
* Global variables

---

# 8. Local Variables

A local variable is created inside a function.

It only exists while the function is running.

Example:

```python
def patient():
    name = "John"
    print(name)

patient()
```

Trying to use `name` outside the function causes a **NameError** because the variable no longer exists.

---

# 9. Global Variables

A global variable is created outside any function.

It can be read inside functions.

Example:

```python
hospital = "Avenue Hospital"

def show():
    print(hospital)

show()
```

**Output**

```
Avenue Hospital
```

---

# 10. Shadowing

If a function creates a local variable with the same name as a global variable, the local variable hides (shadows) the global variable while the function is running.

Example:

```python
hospital = "Avenue Hospital"

def show():
    hospital = "Nairobi Hospital"
    print(hospital)

show()

print(hospital)
```

**Output**

```
Nairobi Hospital
Avenue Hospital
```

The local variable disappears when the function ends.

---

# 11. The global Keyword

Normally, assigning a variable inside a function creates a local variable.

If you want to change the global variable, use the `global` keyword.

Example:

```python
count = 0

def increase():
    global count
    count = count + 1

increase()

print(count)
```

**Output**

```
1
```

Although `global` is useful, professional programmers try to avoid using it too often because it can make programs harder to understand and debug.

---

# 12. Common Errors

## NameError

Occurs when Python cannot find a variable.

Example:

```python
print(patient)
```

---

## UnboundLocalError

Occurs when Python thinks a variable is local but it is used before receiving a value.

Example:

```python
count = 10

def increase():
    count = count + 1
```

---

## TypeError

Occurs when trying to call a variable as if it were a function.

Example:

```python
count = 5

count()
```

Error:

```
TypeError: 'int' object is not callable
```

---

# 13. Mini Project – Hospital Shift Counter

```python
patient_seen = 0

def see_patient():
    global patient_seen
    patient_seen = patient_seen + 1
    print("Patient seen.")
    print("Total patients:", patient_seen)
    print()

see_patient()
see_patient()
see_patient()

print("Final total:", patient_seen)
```

**Output**

```
Patient seen.
Total patients: 1

Patient seen.
Total patients: 2

Patient seen.
Total patients: 3

Final total: 3
```

---

# Key Takeaways

* Functions make code reusable.
* Functions only run when they are called.
* Parameters allow data to be passed into functions.
* `return` sends values back to the program.
* `print()` only displays information.
* Local variables exist only inside a function.
* Global variables exist outside functions.
* Local variables can shadow global variables.
* The `global` keyword allows a function to modify a global variable.
* Reading Python error messages carefully is an important debugging skill.
* Debugging is a normal part of programming and helps you become a better developer.

---

