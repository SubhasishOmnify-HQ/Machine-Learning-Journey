# CSV File Methods and Parameters in Pandas

## Introduction

CSV (Comma-Separated Values) files are the most commonly used data format in Machine Learning. Pandas provides the `read_csv()` function to load and process CSV datasets efficiently. Understanding these parameters helps handle real-world datasets with different structures and formats.

---

# Basic Syntax

```python
import pandas as pd

df = pd.read_csv("dataset.csv")
```

---

# Commonly Used Parameters

## filepath_or_buffer

Specifies the file path.

```python
df = pd.read_csv("data.csv")
```

---

## sep

Defines the delimiter used in the file.

```python
df = pd.read_csv("data.csv", sep=",")
df = pd.read_csv("data.csv", sep=";")
df = pd.read_csv("data.csv", sep="\t")
```

---

## header

Specifies the row number containing column names.

```python
df = pd.read_csv("data.csv", header=0)
df = pd.read_csv("data.csv", header=None)
```

---

## names

Assign custom column names.

```python
df = pd.read_csv("data.csv",
                 names=["ID", "Name", "Age"])
```

---

## index_col

Set a column as the index.

```python
df = pd.read_csv("data.csv", index_col="ID")
```

---

## usecols

Load only selected columns.

```python
df = pd.read_csv("data.csv",
                 usecols=["Name", "Age"])
```

---

## skiprows

Skip specific rows.

```python
df = pd.read_csv("data.csv", skiprows=2)
```

---

## nrows

Read a fixed number of rows.

```python
df = pd.read_csv("data.csv", nrows=100)
```

---

## na_values

Treat specific values as missing.

```python
df = pd.read_csv("data.csv",
                 na_values=["NA", "Missing"])
```

---

## dtype

Specify data types.

```python
df = pd.read_csv("data.csv",
                 dtype={"Age": int})
```

---

## parse_dates

Convert columns into datetime format.

```python
df = pd.read_csv("data.csv",
                 parse_dates=["Date"])
```

---

## converters

Apply custom functions.

```python
df = pd.read_csv("data.csv",
                 converters={"Name": str.upper})
```

---

## encoding

Specify file encoding.

```python
df = pd.read_csv("data.csv",
                 encoding="utf-8")
```

---

## skipinitialspace

Remove spaces after delimiters.

```python
df = pd.read_csv("data.csv",
                 skipinitialspace=True)
```

---

## thousands

Handle thousands separators.

```python
df = pd.read_csv("data.csv",
                 thousands=",")
```

---

## decimal

Specify decimal character.

```python
df = pd.read_csv("data.csv",
                 decimal=".")
```

---

## true_values and false_values

Convert values to Boolean.

```python
df = pd.read_csv(
    "data.csv",
    true_values=["Yes"],
    false_values=["No"]
)
```

---

## comment

Ignore commented lines.

```python
df = pd.read_csv("data.csv",
                 comment="#")
```

---

## chunksize

Read large datasets in chunks.

```python
for chunk in pd.read_csv(
    "data.csv",
    chunksize=1000
):
    print(chunk.head())
```

---

## compression

Read compressed files.

```python
df = pd.read_csv(
    "data.csv.zip",
    compression="zip"
)
```

---

## low_memory

Optimize memory usage.

```python
df = pd.read_csv(
    "data.csv",
    low_memory=False
)
```

---

# Important CSV Operations

## View First Rows

```python
df.head()
```

## View Last Rows

```python
df.tail()
```

## Dataset Information

```python
df.info()
```

## Statistical Summary

```python
df.describe()
```

## Check Missing Values

```python
df.isnull().sum()
```

## Remove Missing Values

```python
df.dropna()
```

## Fill Missing Values

```python
df.fillna(0)
```

## Remove Duplicates

```python
df.drop_duplicates()
```

## Sort Data

```python
df.sort_values("Age")
```

## Save CSV File

```python
df.to_csv("new_data.csv",
          index=False)
```

---

# Importance in Machine Learning

* Data Collection
* Data Cleaning
* Feature Engineering
* Exploratory Data Analysis (EDA)
* Model Training
* Model Evaluation
* Data Storage and Sharing

Mastering CSV handling is one of the most important skills in Machine Learning because almost every real-world project starts with loading, cleaning, and analyzing CSV datasets.
