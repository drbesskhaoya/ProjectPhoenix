# ============================================================

# PROJECT PHOENIX — LESSON 29

# Pandas: Filtering, Selecting & Sorting Data

# ============================================================

"""
LESSON 29 OBJECTIVES
--------------------

By the end of this lesson, you should be able to:

1. Filter DataFrame rows using conditions.
2. Use comparison operators with Pandas.
3. Combine conditions using AND (&) and OR (|).
4. Filter text values.
5. Select specific columns after filtering.
6. Use isin() to match multiple values.
7. Sort DataFrame data using sort_values().
8. Combine multiple Pandas operations into one query.
   """

# ============================================================

# 1. IMPORT PANDAS

# ============================================================

import pandas as pd

# ============================================================

# 2. CREATE A DATAFRAME

# ============================================================

data = {
"Patient": ["Ann", "James", "Sara", "David"],
"Age": [25, 30, 35, 50],
"Diagnosis": [
"Hypertension",
"Malaria",
"Leukemia",
"Diabetes"
]
}

df = pd.DataFrame(data)

print(df)

# ============================================================

# 3. BOOLEAN FILTERING

# ============================================================

# Show patients older than 30.

print(df[df["Age"] > 30])

# Show patients aged 30 or older.

print(df[df["Age"] >= 30])

# ============================================================

# 4. FILTERING TEXT VALUES

# ============================================================

# Show patients diagnosed with Malaria.

print(df[df["Diagnosis"] == "Malaria"])

# Show patients diagnosed with Leukemia.

print(df[df["Diagnosis"] == "Leukemia"])

# ============================================================

# 5. COMBINING CONDITIONS — AND

# ============================================================

# & means AND.

#

# Show patients older than 30 AND diagnosed with Leukemia.

print(
df[
(df["Age"] > 30)
& (df["Diagnosis"] == "Leukemia")
]
)

# ============================================================

# 6. COMBINING CONDITIONS — OR

# ============================================================

# | means OR.

#

# Show patients diagnosed with Malaria OR Diabetes.

print(
df[
(df["Diagnosis"] == "Malaria")
| (df["Diagnosis"] == "Diabetes")
]
)

# ============================================================

# 7. SELECTING SPECIFIC COLUMNS

# ============================================================

# Show only Patient and Diagnosis for patients aged 30 or older.

print(
df[df["Age"] >= 30][["Patient", "Diagnosis"]]
)

# ============================================================

# 8. USING isin()

# ============================================================

# isin() allows us to check whether a value

# belongs to a list of values.

#

# Show patients with Malaria OR Diabetes.

print(
df[
df["Diagnosis"].isin(
["Malaria", "Diabetes"]
)
]
)

# ============================================================

# 9. SORTING DATA

# ============================================================

# Sort from youngest to oldest.

print(
df.sort_values("Age")
)

# Sort from oldest to youngest.

print(
df.sort_values(
"Age",
ascending=False
)
)

# ============================================================

# 10. COMBINING FILTERING + COLUMN SELECTION + SORTING

# ============================================================

# Show Patient and Diagnosis for patients aged 30 or older,

# sorted from oldest to youngest.

print(
df[df["Age"] >= 30]
.sort_values("Age", ascending=False)
[["Patient", "Diagnosis"]]
)

# ============================================================

# 11. PRACTICE

# ============================================================

"""
PRACTICE 1
----------

Display only patients younger than 40.
"""

"""
PRACTICE 2
----------

Display patients diagnosed with Diabetes.
"""

"""
PRACTICE 3
----------

Display patients aged 30 or older AND diagnosed with Malaria.
"""

"""
PRACTICE 4
----------

Display only Patient and Diagnosis for patients
aged 30 or older.
"""

"""
PRACTICE 5
----------

Use isin() to display patients diagnosed with
Malaria or Diabetes.
"""

"""
PRACTICE 6
----------

Sort the DataFrame from oldest to youngest.
"""

# ============================================================

# 12. MINI-PROJECT — CLINIC PATIENT FILTER

# ============================================================

"""
Scenario
--------

You are reviewing a clinic patient dataset.

Your task is to identify patients who:

```
- Are aged 30 or older
- Have either Malaria or Diabetes
- Are displayed from oldest to youngest
- Show only Patient and Diagnosis
```

Expected result:

```
Patient    Diagnosis
David      Diabetes
Mary       Malaria
James      Malaria
```

"""

# Create an expanded dataset.

clinic_data = {
"Patient": ["Ann", "James", "Sara", "David", "Mary"],
"Age": [25, 30, 35, 50, 42],
"Diagnosis": [
"Hypertension",
"Malaria",
"Leukemia",
"Diabetes",
"Malaria"
]
}

clinic_df = pd.DataFrame(clinic_data)

# Complete solution:

result = (
clinic_df[
(clinic_df["Age"] >= 30)
& (
clinic_df["Diagnosis"].isin(
["Malaria", "Diabetes"]
)
)
]
.sort_values("Age", ascending=False)
[["Patient", "Diagnosis"]]
)

print(result)

# ============================================================

# 13. KEY TAKEAWAYS

# ============================================================

"""
PANDAS FILTERING CHEAT SHEET
----------------------------

Filter rows:

```
df[df["Age"] > 30]
```

Greater than:

```
>
```

Greater than or equal:

```
>=
```

Equal to:

```
==
```

Less than:

```
<
```

Less than or equal:

```
<=
```

AND:

```
&
```

OR:

```
|
```

Multiple possible values:

```
df["Diagnosis"].isin(["Malaria", "Diabetes"])
```

Select specific columns:

```
df[["Patient", "Diagnosis"]]
```

Sort ascending:

```
df.sort_values("Age")
```

Sort descending:

```
df.sort_values("Age", ascending=False)
```

IMPORTANT:
When combining conditions, place each condition
inside parentheses.

Example:

```
df[
    (df["Age"] >= 30)
    & (df["Diagnosis"] == "Malaria")
]
```

## CORE PATTERN

Filter:

```
df[condition]
```

Filter + select columns:

```
df[condition][["Column1", "Column2"]]
```

Filter + sort + select:

```
df[condition]
  .sort_values("Age", ascending=False)
  [["Column1", "Column2"]]
```

## LESSON 29 COMPLETE

You can now ask practical questions of a DataFrame,
filter the relevant patients, select the information
you need, and sort the results.

This is an important foundation for working with
real-world healthcare datasets.
"""

# ============================================================

# END OF LESSON 29

# ============================================================
