"""
=========================================================
Project Phoenix – Week 2 – Lesson 17
Python Standard Library Essentials
(datetime • statistics • csv • json • pathlib)
=========================================================

Author : Project Phoenix
Purpose:
Learn how to work with Python's built-in Standard Library modules for
real-world data processing.

These modules are used extensively in:

• Healthcare AI
• Data Engineering
• Machine Learning
• Clinical Research
• Automation
• Backend Development

---------------------------------------------------------
TOPICS COVERED
---------------------------------------------------------

1. datetime
    - datetime.now()
    - datetime.today()
    - attributes
    - strftime()
    - timedelta()

2. statistics
    - mean()
    - median()
    - mode()
    - stdev()

3. csv
    - csv.reader()
    - csv.DictReader()
    - next(reader)

4. json
    - json.dumps()
    - json.loads()

5. pathlib
    - Path()
    - exists()
    - read_text()

6. Healthcare Mini Project
    Patient Analytics Dashboard

"""

# =========================================================
# IMPORTS
# =========================================================

from datetime import datetime, timedelta
from pathlib import Path
import statistics
import csv
import json

# =========================================================
# PART 1 — DATETIME
# =========================================================

"""
The datetime module allows Python programs to work with:

• Current date
• Current time
• Future dates
• Past dates
• Date calculations
• Formatting

Healthcare Examples

✔ Appointment scheduling
✔ Follow-up reminders
✔ Patient admission dates
✔ Medication timing
✔ Surgery booking
✔ Laboratory timestamps
"""

print("\n==============================")
print("PART 1 — DATETIME")
print("==============================")

current = datetime.now()

print(current)

# ---------------------------------------------------------
# Current Date
# ---------------------------------------------------------

print("\nToday's date:")

print(current.date())

# ---------------------------------------------------------
# Current Time
# ---------------------------------------------------------

print("\nCurrent time:")

print(current.time())

# ---------------------------------------------------------
# Individual Attributes
# ---------------------------------------------------------

print("\nDatetime attributes")

print("Year :", current.year)
print("Month:", current.month)
print("Day  :", current.day)
print("Hour :", current.hour)
print("Min  :", current.minute)
print("Sec  :", current.second)

# ---------------------------------------------------------
# today()
# ---------------------------------------------------------

today = datetime.today()

print("\ndatetime.today()")
print(today)

"""
datetime.now()

Returns the current local date and time.

datetime.today()

Returns the current local date and time.

Both are extremely similar.

Most modern code uses datetime.now().
"""

# ---------------------------------------------------------
# Formatting Dates
# ---------------------------------------------------------

print("\nFormatted Date")

formatted = current.strftime("%d/%m/%Y")

print(formatted)

formatted = current.strftime("%A")

print(formatted)

formatted = current.strftime("%d %B %Y")

print(formatted)

formatted = current.strftime("%I:%M %p")

print(formatted)

"""
Common format codes

%d   Day

%m   Month number

%B   Full month

%Y   Four-digit year

%A   Weekday

%H   24-hour clock

%I   12-hour clock

%M   Minutes

%S   Seconds

%p   AM / PM
"""

# ---------------------------------------------------------
# timedelta
# ---------------------------------------------------------

print("\nTimedelta")

today = datetime.now()

follow_up = today + timedelta(days=14)

print("Today     :", today.strftime("%d-%m-%Y"))

print("Follow Up :", follow_up.strftime("%d-%m-%Y"))

"""
timedelta is used to add or subtract time.

Examples

+ days
+ hours
+ minutes
+ weeks

Healthcare uses

Medication reviews

Follow-up appointments

Vaccination schedules

ICU monitoring intervals

Prescription expiry
"""

# =========================================================
# SENIOR ENGINEER NOTES
# =========================================================

"""
Best Practice

Store actual datetime objects.

Only format them when displaying to users.

Good

appointment = datetime.now()

Bad

appointment = "08/08/2026"

Strings cannot perform date calculations easily.
"""

# =========================================================
# HEALTHCARE AI CONNECTION
# =========================================================

"""
Healthcare AI systems constantly use datetime.

Examples

Patient monitoring

ICU vital timestamps

Radiology report generation

Medication reminders

Emergency department waiting times

Machine learning models often engineer features such as

Hour of admission

Weekend admission

Length of stay

Time since surgery
"""

# =========================================================
# PART 2 — STATISTICS
# =========================================================

print("\n==============================")
print("PART 2 — STATISTICS")
print("==============================")

"""
The statistics module performs common mathematical calculations.

Useful for

Clinical audits

Research

Hospital dashboards

Machine learning preprocessing
"""

heart_rates = [72, 78, 85, 80, 76, 81]

print(heart_rates)

# ---------------------------------------------------------
# Mean
# ---------------------------------------------------------

average = statistics.mean(heart_rates)

print("\nMean")

print(average)

# ---------------------------------------------------------
# Median
# ---------------------------------------------------------

middle = statistics.median(heart_rates)

print("\nMedian")

print(middle)

# ---------------------------------------------------------
# Mode
# ---------------------------------------------------------

scores = [1, 2, 2, 3, 3, 3, 4]

print("\nMode")

print(statistics.mode(scores))

# ---------------------------------------------------------
# Standard Deviation
# ---------------------------------------------------------

print("\nStandard Deviation")

print(statistics.stdev(heart_rates))

"""
Mean

Average value

Median

Middle value

Mode

Most common value

Standard Deviation

Measures spread or variability.

Small stdev

Values are close together.

Large stdev

Values vary widely.
"""

# =========================================================
# SENIOR ENGINEER NOTES
# =========================================================

"""
Always validate data before calculating statistics.

Empty lists cause errors.

Example

if heart_rates:

    print(statistics.mean(heart_rates))
"""

# =========================================================
# HEALTHCARE AI CONNECTION
# =========================================================

"""
Statistics is everywhere.

Examples

Average patient age

Average waiting time

Average blood pressure

Average glucose level

Predictive modelling

Disease surveillance

Clinical trials
"""

# =========================================================
# PART 3 — CSV
# =========================================================

print("\n==============================")
print("PART 3 — CSV")
print("==============================")

"""
CSV

Comma Separated Values

A CSV file stores data like:

name,age,heart_rate
John,34,80
Mary,50,75
Peter,22,71

CSV is one of the most common healthcare data formats.
"""

# ---------------------------------------------------------
# csv.reader()
# ---------------------------------------------------------

print("\nExample using csv.reader()")

sample_file = "patients.csv"

"""
Suppose patients.csv contains

name,age,heart_rate
John,45,80
Mary,38,72
Peter,60,91
"""

try:

    with open(sample_file, newline="") as file:

        reader = csv.reader(file)

        header = next(reader)

        print("Header:", header)

        for row in reader:

            print(row)

except FileNotFoundError:

    print("patients.csv not found (example only).")

"""
csv.reader()

Returns each row as a LIST.

Example

['John','45','80']
"""

# ---------------------------------------------------------
# DictReader
# ---------------------------------------------------------

print("\nExample using csv.DictReader()")

try:

    with open(sample_file, newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            print(row)

except FileNotFoundError:

    print("patients.csv not found (example only).")

"""
DictReader returns dictionaries.

Example

{
'name':'John',
'age':'45',
'heart_rate':'80'
}

This is easier to read and much safer.
"""

# =========================================================
# SENIOR ENGINEER NOTES
# =========================================================

"""
Prefer DictReader over csv.reader.

Why?

reader

row[0]

row[1]

row[2]

Hard to remember.

DictReader

row["name"]

row["age"]

row["heart_rate"]

Far more readable.
"""

# =========================================================
# HEALTHCARE AI CONNECTION
# =========================================================

"""
Hospitals export huge amounts of data as CSV.

Examples

Admissions

Laboratory results

Radiology reports

Drug inventories

Outpatient visits

CSV files are frequently the first step before data enters
machine learning pipelines.
"""

# =========================================================
# PART 4 — JSON
# =========================================================

print("\n==============================")
print("PART 4 — JSON")
print("==============================")

"""
JSON

JavaScript Object Notation

The universal language for APIs.

Almost every modern application exchanges data using JSON.
"""

patient = {

    "name": "John",

    "age": 45,

    "diagnosis": "Hypertension"

}

# ---------------------------------------------------------
# dumps
# ---------------------------------------------------------

json_string = json.dumps(patient, indent=4)

print("\nJSON String")

print(json_string)

# ---------------------------------------------------------
# loads
# ---------------------------------------------------------

python_object = json.loads(json_string)

print("\nConverted back to Python")

print(python_object)

"""
dumps()

Python dictionary

↓

JSON string

loads()

JSON string

↓

Python dictionary
"""

# =========================================================
# SENIOR ENGINEER NOTES
# =========================================================

"""
Remember

dump()

Writes JSON to a file.

dumps()

Returns a JSON string.

load()

Reads JSON from a file.

loads()

Reads from a JSON string.
"""

# =========================================================
# HEALTHCARE AI CONNECTION
# =========================================================

"""
Electronic Health Records

FHIR

Hospital APIs

Mobile healthcare apps

Wearables

Remote monitoring devices

Almost all exchange information using JSON.
"""

# =========================================================
# PART 5 — PATHLIB
# =========================================================

print("\n==============================")
print("PART 5 — PATHLIB")
print("==============================")

"""
pathlib provides a modern way of working with files.

Instead of manipulating strings,
Python represents files as Path objects.
"""

file = Path("patients.txt")

print(file)

# ---------------------------------------------------------
# exists()
# ---------------------------------------------------------

print("\nDoes file exist?")

print(file.exists())

# ---------------------------------------------------------
# read_text()
# ---------------------------------------------------------

if file.exists():

    print("\nContents")

    print(file.read_text())

else:

    print("Example file not found.")

"""
Useful methods

exists()

read_text()

write_text()

mkdir()

unlink()

glob()

suffix

stem

name
"""

# =========================================================
# SENIOR ENGINEER NOTES
# =========================================================

"""
Modern Python prefers pathlib over os.path.

It is

Cleaner

Safer

Object-oriented

Cross-platform
"""

# =========================================================
# HEALTHCARE AI CONNECTION
# =========================================================

"""
Healthcare AI projects often process thousands of files.

Examples

MRI images

CT scans

CSV datasets

JSON reports

Clinical notes

Pathlib simplifies handling these files.
"""

# =========================================================
# COMMON MISTAKES
# =========================================================

"""
1.

Using datetime as a variable name.

Wrong

datetime = 5

This overwrites the imported module.

--------------------------------------------------

2.

Formatting dates too early.

Keep datetime objects until display.

--------------------------------------------------

3.

Using statistics.mean() on an empty list.

Always validate first.

--------------------------------------------------

4.

Forgetting next(reader)

This causes the header row to be treated as patient data.

--------------------------------------------------

5.

Confusing csv.reader with DictReader.

reader

Returns LISTS.

DictReader

Returns DICTIONARIES.

--------------------------------------------------

6.

Confusing dumps and dump.

dumps()

Returns text.

dump()

Writes to file.

--------------------------------------------------

7.

Confusing loads and load.

loads()

Reads JSON string.

load()

Reads JSON file.

--------------------------------------------------

8.

Using ordinary strings instead of Path objects.

Prefer

Path("patients.txt")

instead of

"patients.txt"

--------------------------------------------------

Mistakes we encountered during Lesson 17

✔ Forgetting to skip the CSV header.

✔ Mixing up rows returned as lists versus dictionaries.

✔ Confusing json.dumps() with json.loads().

✔ Forgetting that Path.read_text() requires the file to exist.

✔ Treating formatted date strings as datetime objects.
"""

# =========================================================
# PRACTICE EXERCISES
# =========================================================

"""
Exercise 1

Print today's weekday.

-----------------------------------

Exercise 2

Calculate a follow-up date 30 days from today.

-----------------------------------

Exercise 3

Find the mean blood pressure from

[120,125,118,130,128]

-----------------------------------

Exercise 4

Create a dictionary describing a patient
and convert it to JSON.

-----------------------------------

Exercise 5

Read a text file using pathlib.

-----------------------------------

Exercise 6

Read a CSV file using DictReader and
print each patient's name.
"""

# =========================================================
# MINI PROJECT
# =========================================================

print("\n==============================")
print("MINI PROJECT")
print("Patient Analytics Dashboard")
print("==============================")

"""
PROJECT GOALS

✔ pathlib
✔ csv.DictReader
✔ statistics
✔ datetime
✔ timedelta
✔ json

This project demonstrates how multiple
standard library modules work together in a
real-world healthcare scenario.
"""

# ---------------------------------------------------------
# STEP 1 — CREATE SAMPLE CSV (IF NEEDED)
# ---------------------------------------------------------

csv_path = Path("patient_dashboard.csv")

if not csv_path.exists():

    csv_path.write_text(
        """name,age,heart_rate
John,45,80
Mary,38,72
Peter,60,91
Alice,29,76
David,55,88
"""
    )

# ---------------------------------------------------------
# STEP 2 — READ CSV
# ---------------------------------------------------------

patients = []

heart_rates = []

ages = []

with csv_path.open(newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        row["age"] = int(row["age"])
        row["heart_rate"] = int(row["heart_rate"])

        patients.append(row)

        ages.append(row["age"])
        heart_rates.append(row["heart_rate"])

# ---------------------------------------------------------
# STEP 3 — CALCULATE STATISTICS
# ---------------------------------------------------------

average_age = statistics.mean(ages)
average_hr = statistics.mean(heart_rates)
median_hr = statistics.median(heart_rates)
stdev_hr = statistics.stdev(heart_rates)

# ---------------------------------------------------------
# STEP 4 — REPORT DATE
# ---------------------------------------------------------

generated = datetime.now()

next_review = generated + timedelta(days=30)

# ---------------------------------------------------------
# STEP 5 — BUILD REPORT
# ---------------------------------------------------------

report = {

    "generated":

        generated.strftime("%d-%m-%Y %H:%M"),

    "next_review":

        next_review.strftime("%d-%m-%Y"),

    "total_patients":

        len(patients),

    "average_age":

        round(average_age, 1),

    "average_heart_rate":

        round(average_hr, 1),

    "median_heart_rate":

        median_hr,

    "heart_rate_stdev":

        round(stdev_hr, 2),

    "patients":

        patients

}

# ---------------------------------------------------------
# STEP 6 — DISPLAY REPORT
# ---------------------------------------------------------

print(json.dumps(report, indent=4))

# ---------------------------------------------------------
# STEP 7 — SAVE JSON REPORT
# ---------------------------------------------------------

json_path = Path("patient_dashboard_report.json")

json_path.write_text(json.dumps(report, indent=4))

print("\nDashboard saved to:")

print(json_path)

# =========================================================
# KEY TAKEAWAYS
# =========================================================

"""
After Lesson 17 you should understand:

✔ Working with dates using datetime

✔ Formatting dates using strftime()

✔ Date calculations using timedelta()

✔ Statistical calculations using statistics

✔ Reading CSV files

✔ Why DictReader is preferred

✔ Converting Python objects to JSON

✔ Converting JSON back to Python

✔ Using pathlib to manage files

✔ Combining multiple standard library modules
   into a complete real-world application

This lesson marks an important transition from
basic Python programming to professional software
development using the Python Standard Library.
"""

# =========================================================
# END OF LESSON 17
# =========================================================

"""
Congratulations!

You have completed Lesson 17.

You can now build programs that:

✔ Process CSV datasets

✔ Analyse healthcare information

✔ Generate JSON reports

✔ Schedule future events

✔ Read files safely

✔ Build reusable analytics tools

---------------------------------------------------------

LESSON 18 PREVIEW

Next we begin Object-Oriented Programming (OOP).

Topics include:

• Classes
• Objects
• Attributes
• Methods
• Constructors (__init__)
• Instance variables
• Class design
• Building a Hospital Management System using OOP

Object-Oriented Programming is one of the most
important milestones in Python and forms the
foundation of large software projects, backend
systems, AI frameworks, and enterprise healthcare
applications.


"""