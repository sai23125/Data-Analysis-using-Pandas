# Data-Analysis-using-Pandas
# Data Analysis using Pandas

## Description

This project demonstrates basic data analysis using Python and the Pandas library. It loads a CSV dataset, inspects the data, cleans missing values, filters records, performs grouping and aggregation, and provides simple insights from the dataset.

## Features

- Load CSV dataset
- Inspect dataset information
- Handle missing values
- Filter records
- Group data by department
- Calculate average, minimum, maximum, and employee count
- Generate simple data insights

## Technologies Used

- Python 3
- Pandas

## Project Structure

```
DataAnalysis/
│── data_analysis.py
│── employees.csv
└── README.md
```

## How to Run

1. Clone the repository.

```
git clone https://github.com/yourusername/data-analysis-python.git
```

2. Install Pandas.

```
pip install pandas
```

3. Run the script.

```
python data_analysis.py
```

## Dataset

The dataset contains employee information such as:
- Employee ID
- Name
- Department
- Age
- Salary

## Insights

- Missing values are cleaned using the average of the respective columns.
- Employees with salaries greater than ₹45,000 are identified.
- The IT department has the highest average salary.
- Grouping and aggregation help compare departments effectively.

## Learning Outcomes

- Data loading and inspection
- Data cleaning
- Filtering datasets
- Grouping and aggregation
- Basic exploratory data analysis using Pandas
