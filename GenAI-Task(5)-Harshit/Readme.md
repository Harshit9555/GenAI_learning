# Python Modules and Packages Assignment

## Overview
This assignment demonstrates the creation and implementation of Python modules and packages. It covers importing modules in different ways, creating reusable functions, and organizing Python code using packages.

## Project Structure

```text
GenAI-Task(5)-Harshit/
│
├── Task1/
│   ├── main.py
│   └── math_utils.py
│
├── Task2/
│   ├── main.py
│   └── string_utils.py
│
├── Task3/
│   ├── test_package.py
│   └── shop_package/
│       ├── __init__.py
│       ├── discount.py
│       └── billing.py
│
├── Task4/
│   ├── main.py
│   └── shop_package/
│       ├── __init__.py
│       ├── discount.py
│       └── billing.py
│
└── README.md
```

## Task 1: Create a Simple Module (math_utils.py)

Created a Python module named `math_utils.py` containing three functions:

- `add(a, b)`: Returns the sum of two numbers.
- `subtract(a, b)`: Returns the difference between two numbers.
- `square(n)`: Returns the square of a number.

**Import methods used:**
```python
import math_utils
from math_utils import square
```

**Output:**
```text
Addition: 15
Subtraction: 5
Square: 25
```

## Task 2: Create Another Module (string_utils.py)

Created a Python module named `string_utils.py` containing three string operations:

- `capitalize_words(text)`: Capitalizes the first letter of each word.
- `reverse_string(text)`: Reverses the given string.
- `word_count(text)`: Counts the number of words in a string.

**Import statement:**
```python
import string_utils
```

**Output:**
```text
Capitalized: Hello Python World
Reversed: dlrow nohtyp olleh
Word Count: 3
```

## Task 3: Create a Simple Package (shop_package)

Created a package named `shop_package` containing two Python modules.

### 1. discount.py

Contains the following functions:

- `apply_discount(price, percent)`: Calculates the price after applying a percentage discount.
- `flat_discount(price)`: Subtracts a fixed amount of 50 from the price.

### 2. billing.py

Contains the following functions:

- `calculate_total(prices)`: Calculates the total bill by adding all prices.
- `apply_tax(amount)`: Adds 5% tax to the given amount.

### 3. __init__.py

Used to initialize the package and export its functions.

```python
from .discount import apply_discount, flat_discount
from .billing import calculate_total, apply_tax
```

**Output:**
```text
Percentage Discount: 900.0
Flat Discount: 950
Total Bill: 600
Tax: 630.0
```

## Task 4: Importing the Package in main.py

Imported the package using different import techniques.

**Import statements:**
```python
import shop_package.discount as disc
from shop_package.billing import calculate_total
from shop_package.billing import apply_tax
```

Called all four functions to test the package.

**Output:**
```text
Percentage Discount: 900.0
Flat Discount: 950
Total Bill: 600
Tax: 630.0
```

## Technologies Used

- Programming Language: Python
- IDE: Visual Studio Code
- Terminal: Windows PowerShell

## How to Run the Programs

1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Navigate to the required task folder.
4. Execute the Python file using:

```bash
python main.py
```

For Task 3, run:

```bash
python test_package.py
```

## Conclusion

Through this assignment, I learned how to create Python modules, define reusable functions, import modules using different methods, create packages, and organize Python programs into multiple files. I also understood the importance of the `__init__.py` file in package initialization and how Python handles package imports.