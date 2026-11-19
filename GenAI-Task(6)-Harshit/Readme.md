# Python Exception Handling – Assignment

## Overview
This assignment covers Python Exception Handling concepts using practical programming tasks. It demonstrates how to handle runtime errors, raise custom exceptions, and ensure smooth program execution using `try`, `except`, `else`, and `finally` blocks.

## Questions

### Task 1: Safe Division Utility
**Objective:** Create a safe division program using exception handling.

**Requirements:**
- Take numerator and denominator as user inputs.
- Handle `ValueError` if the input is not a number.
- Handle `ZeroDivisionError` if the denominator is zero.
- Use the `else` block to print the division result if no error occurs.
- Use the `finally` block to print "Operation Complete".

**Concepts Used:**
- try-except
- ValueError
- ZeroDivisionError
- else and finally blocks

### Task 2: Bill Calculator with Error Handling
**Objective:** Calculate the total bill using a list of product prices while handling invalid values.

**Input:**
```python
prices = [120, 350, 'abc', 500, -200, 800]
```

**Requirements:**
- Iterate through the list.
- Add only valid positive numerical prices.
- Handle `TypeError` if a value is not a number.
- Raise a custom `ValueError` for negative prices.
- Print the running total.
- Skip invalid items and continue processing.

**Expected Final Bill:** 1770

**Concepts Used:**
- for loop
- TypeError
- Custom ValueError
- raise statement
- Exception handling

### Task 3: Custom Exception – Age Validator
**Objective:** Create a function to validate a person's age.

**Requirements:**
- Create a function named `check_age(age)`.
- Raise a custom `ValueError` if age is less than 1 or greater than 120.
- Take age as input from the user.
- Use try-except to catch and print the custom error message.
- Print the age if it is valid.

**Error Message:**
```text
Age must be between 1 and 120
```

**Concepts Used:**
- Functions
- Custom exceptions
- ValueError
- raise statement
- try-except

### Task 4: File Reader with Exception Handling
**Objective:** Read a file and handle file-related exceptions.

**Requirements:**
- Ask the user to enter a filename.
- Open and read the file.
- Handle `FileNotFoundError` if the file does not exist.
- Handle `PermissionError` if access is denied.
- If successful, print the first three lines of the file.
- Use the finally block to print "File operation attempted."

**Concepts Used:**
- File handling
- open()
- readlines()
- FileNotFoundError
- PermissionError
- finally block

### Task 5: Mini Program – Safe Shopping Cart
**Objective:** Create a shopping cart program with input validation and exception handling.

**Requirements:**
- Create an empty cart list.
- Use a loop to accept product prices from the user.
- Stop the loop when the user enters 'q'.
- Convert each valid input into a float.
- Handle `ValueError` for invalid inputs.
- Raise a custom `ValueError` if the price is negative.
- At the end, display the total number of items and total bill.

**Concepts Used:**
- Lists
- while loop
- float()
- append()
- ValueError
- Custom exceptions
- sum() and len()

## Python Concepts Covered

| Concept | Description |
|---|---|
| try | Executes code that may generate an exception |
| except | Handles exceptions |
| else | Executes when no exception occurs |
| finally | Always executes |
| raise | Manually raises an exception |
| ValueError | Handles invalid values |
| TypeError | Handles incompatible data types |
| FileNotFoundError | Handles missing files |
| PermissionError | Handles permission issues |

## Learning Outcomes

After completing this assignment, I learned:

1. How to handle runtime errors in Python.
2. How to use try-except-else-finally blocks.
3. How to create and raise custom exceptions.
4. How to validate user input.
5. How to handle file-related exceptions.
6. How to build reliable programs using exception handling.

## Technologies Used
- **Programming Language:** Python
- **Editor:** Visual Studio Code
- **Concept:** Python Exception Handling

## Conclusion

This assignment helped me understand Python exception handling and error management through practical programming exercises. It improved my ability to write robust, reliable, and error-free Python programs.