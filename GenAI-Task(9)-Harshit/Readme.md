# NumPy Assignment – Python Numerical Computing

## Overview
This project covers the fundamentals of NumPy (Numerical Python), including array creation, mathematical operations, statistical calculations, aggregation, sorting, percentiles, and basic sales data analysis.

The assignment demonstrates how NumPy can efficiently perform numerical computations using arrays and built-in mathematical functions.

## Technologies Used
- Python 3.x
- NumPy

## Installation

Install NumPy using pip:

```bash
pip install numpy
```

Import NumPy into your Python program:

```python
import numpy as np
```

## Tasks Covered

### Task 1: Creating NumPy Arrays
- Create a 1D integer array from 1 to 10.
- Create a 2D array of shape (3, 3) with values from 1 to 9.
- Create a NumPy array from the list `[10, 20, 30, 40, 50]`.
- Display the shape and data type of each array.

### Task 2: Important Mathematical Operations
Perform mathematical operations on two arrays:

```python
A = np.array([10, 20, 30, 40])
B = np.array([1, 2, 3, 4])
```

Operations:
- Addition (A + B)
- Subtraction (A - B)
- Multiplication (A * B)
- Division (A / B)
- Power (A ** 2)

Also explore NumPy functions such as `np.add()` and `np.subtract()`.

### Task 3: Important NumPy Mathematical Formulas

Given:

```python
values = np.array([2, 4, 6, 8, 10])
```

Calculate:
- Square root using `np.sqrt()`
- Exponential using `np.exp()`
- Natural logarithm using `np.log()`
- Sum using `np.sum()`
- Cumulative sum using `np.cumsum()`

### Task 4: Aggregation Operations

Given a 2D array:

```python
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

Calculate:
- Row-wise sum using `np.sum(data, axis=1)`
- Column-wise sum using `np.sum(data, axis=0)`
- Minimum value using `np.min()`
- Maximum value using `np.max()`
- Overall mean using `np.mean()`

### Task 5: Statistical Operations

Given:

```python
marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])
```

Calculate:
1. Mean using `np.mean()`
2. Median using `np.median()`
3. Variance using `np.var()`
4. Standard deviation using `np.std()`
5. Minimum and maximum using `np.min()` and `np.max()`
6. Range (Maximum - Minimum)

### Task 6: Percentiles & Sorting

Using the same marks array:
- Sort the array using `np.sort()`.
- Calculate the 25th percentile using `np.percentile(marks, 25)`.
- Calculate the 50th percentile using `np.percentile(marks, 50)`.
- Calculate the 75th percentile using `np.percentile(marks, 75)`.
- Count the number of students scoring above average using NumPy conditions and `np.sum()`.

### Task 7: Mini Use Case – Sales Analysis

Given daily sales data:

```python
sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])
```

Perform the following operations:
1. Calculate total weekly sales using `np.sum()`.
2. Calculate