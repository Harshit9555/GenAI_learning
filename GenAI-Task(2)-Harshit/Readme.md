# Python Control Flow and Looping Tasks

## 📌 Overview
This repository contains Python programming tasks focused on conditional statements, loops, user input handling, discount calculations, and loop control using `break` and `continue`. The programs are implemented in a Jupyter Notebook (`.ipynb`).

## 🎯 Objectives
- Understand `if`, `elif`, and `else` statements.
- Apply discount rules to order amounts.
- Handle invalid user input using exception handling.
- Process multiple orders using `for` loops.
- Calculate total revenue after discounts.
- Build a menu-driven program using `while` loops.
- Understand the use of `break` and `continue` in loops.

## 📝 Tasks Covered

### Task 1: Discount Rules
Accept an integer order amount and apply the following discount rules:

| Order Amount | Discount |
|---|---:|
| ₹2,000 or more | 15% |
| ₹1,500–₹1,999 | 10% |
| ₹1,000–₹1,499 | 7% |
| Below ₹1,000 | 0% |

**Features:**
- Calculate the final amount after discount.
- Handle non-numeric input with an error message.
- Optional: Calculate 5% tax after discount and display the subtotal, tax, and final total.

### Task 2: Process Multiple Orders
Process a predefined list of order amounts using a `for` loop.

```python
orders = [1200, 2500, 800, 1750, 3000]
```

**Features:**
- Apply the discount rules to each order.
- Display the order amount, discount percentage, and final amount.
- Calculate total revenue after discounts.
- Optional: Count the number of orders that received a discount.

### Task 3: Menu-Driven Program
Create an interactive program using a `while` loop.

**Menu Options:**
- `1` — Add an order amount.
- `2` — Display all orders and the total after discounts.
- `q` — Quit the program.

**Features:**
- Store orders in a list.
- Calculate discounts and maintain running revenue.
- Use `break` to exit the loop.
- Use `continue` to handle invalid input and return to the menu.

### Task 4: Loop Control with Conditions
Process daily sales using a `for` loop.

```python
daily = [200, 150, 0, 400, 50, -1, 300]
```

**Rules:**
- If a sales value is `-1`, treat it as corrupted data and stop processing using `break`.
- If a sales value is `0`, skip that day using `continue`.
- Add valid positive sales to the running total.
- Print the running total and the final total after processing stops or completes.

## 🛠️ Technologies Used
- **Language:** Python
- **Environment:** Jupyter Notebook
- **Concepts:** Conditional statements, `for` loops, `while` loops, lists, exception handling, arithmetic operations, `break`, and `continue`.

## ▶️ How to Run
1. Clone or download this repository.
2. Open the `.ipynb` file in Jupyter Notebook, JupyterLab, or Google Colab.
3. Run the notebook cells sequentially.
4. Enter the required inputs when prompted.
5. Review the calculated discounts, final order amounts, and revenue totals.

## 📚 Learning Outcomes
After completing these tasks, you will understand how to:
- Implement business rules using conditional statements.
- Process and analyze multiple orders.
- Build interactive, menu-driven programs.
- Validate user input and handle errors.
- Control loop execution using `break` and `continue`.

## 👨‍💻 Author
Harshit Mishra
