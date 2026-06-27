# ---------------------------------------------------
# CSV Data Analysis using Pandas
# Author: B.Sai pavan
# ---------------------------------------------------

import pandas as pd

# -------------------------------
# Load CSV Dataset
# -------------------------------
try:
    df = pd.read_csv("employees.csv")
    print("Dataset Loaded Successfully\n")
except FileNotFoundError:
    print("employees.csv not found!")
    exit()

# -------------------------------
# Inspect Dataset
# -------------------------------
print("First Five Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

# -------------------------------
# Clean Missing Data
# -------------------------------

# Fill missing Age with average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Salary with average salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nDataset After Cleaning")
print(df)

# -------------------------------
# Filtering
# -------------------------------

print("\nEmployees with Salary greater than 45000")

high_salary = df[df["Salary"] > 45000]

print(high_salary)

# -------------------------------
# Grouping and Aggregation
# -------------------------------

print("\nAverage Salary by Department")

avg_salary = df.groupby("Department")["Salary"].mean()

print(avg_salary)

print("\nEmployee Count by Department")

employee_count = df.groupby("Department")["EmployeeID"].count()

print(employee_count)

print("\nMaximum Salary by Department")

max_salary = df.groupby("Department")["Salary"].max()

print(max_salary)

print("\nMinimum Salary by Department")

min_salary = df.groupby("Department")["Salary"].min()

print(min_salary)

print("\nProgram Completed Successfully")