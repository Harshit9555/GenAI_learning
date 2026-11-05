## 📌 Project Overview

This project demonstrates basic Python file handling operations, including writing, reading, appending data, generating summary reports, handling missing files, and exporting discounted product prices.

The project uses Python's built-in functions and modules without requiring advanced libraries.

## 🎯 Tasks Covered

### Task 1: Write Sales Records to a File
- Create a list of sales amounts: `1200, 450, 980, 1500, 3000`.
- Write the sales records to `sales_data.txt`.
- Store each sale on a new line.
- Read and print the file contents.

### Task 2: Read File in Different Ways
- Read the entire file using `read()`.
- Read the first line using `readline()`.
- Read all lines using `readlines()`.
- Convert the sales values into a list of integers.
- Clean up newline characters using `strip()`.

### Task 3: Append New Sales
- Append new sales records: `5000, 2500, 1700`.
- Preserve the existing sales records.
- Read and display the updated file.
- Count the total number of lines.

### Task 4: Generate Summary Report
Read sales records from `sales_data.txt` and calculate:
- Total Sales
- Highest Sale
- Lowest Sale
- Average Sale

### Task 5: Create Product Info File
- Accept three product names and their prices from the user.
- Write the information to `products.txt`.
- Use the format `ProductName | Price`.
- Read and display the saved product information.

### Task 6: Read File Safely
- Ask the user for a filename.
- Check whether the file exists using `os.path.exists()`.
- Display the file contents if it exists.
- Print an appropriate message if the file is missing.

### Task 7: Export Discounted Prices
- Store product prices in a dictionary.
- Accept a discount percentage from the user.
- Calculate discounted prices for all products.
- Export the results to `discount_report.txt`.
- Display the report in the terminal.
- Include the total number of items and average discounted price.

## 🛠️ Technologies Used

- **Language:** Python
- **Concepts:** File Handling, Lists, Dictionaries, Loops, Conditional Statements, User Input, Type Conversion, Basic Calculations
- **Built-in Functions:** `open()`, `read()`, `readline()`, `readlines()`, `write()`, `sum()`, `min()`, `max()`, `len()`
- **Module:** `os`


## ▶️ How to Run

### Option 1: Python File

1. Install Python on your system.
2. Clone or download this repository.
3. Open the project folder in VS Code or a terminal.
4. Run:

```bash
python file_handling_tasks.py
```

### Option 2: Jupyter Notebook

1. Open `file_handling_tasks.ipynb` in Jupyter Notebook.
2. Run each cell in order.
3. Enter the requested product information and discount percentage when prompted.
4. Check the generated text files in the notebook's working directory.

## 📊 Sample Sales Data

```text
1200
450
980
1500
3000
5000
2500
1700
```

## 📚 Learning Outcomes

After completing these tasks, you will understand how to:

- Create and manage text files in Python.
- Use file modes such as read (`r`), write (`w`), and append (`a`).
- Read and write structured text data.
- Convert strings into integers and floating-point numbers.
- Calculate basic statistics from file data.
- Check whether files exist before reading them.
- Generate simple reports and export calculated results.

## 👨‍💻 Author

**Harshit Mishra**

---

⭐ If you find this project useful, consider giving the repository a star!
