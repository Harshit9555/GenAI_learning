# Python Object-Oriented Programming (OOP) – Assignment

## Overview
This repository contains 7 Python programming tasks based on Object-Oriented Programming (OOP) concepts. The assignment demonstrates classes, objects, constructors, encapsulation, inheritance, polymorphism, abstraction, magic methods, operator overloading, and a mini inventory management system.

## Technologies Used
- **Programming Language:** Python 3
- **Concepts:** Object-Oriented Programming (OOP)
- **Tools:** VS Code / PyCharm / Jupyter Notebook

---

## Tasks Covered

### Task 1: Basic Class & Object Creation
**Concept:** Classes and Objects

- Create a `Product` class.
- Attributes: `name`, `price`, `category`.
- Implement `get_info()` to display product details.
- Create two objects and call their methods.
- Extra: Implement `apply_discount(percent)` to calculate the discounted price.

### Task 2: Constructor & Encapsulation
**Concept:** Constructor and Data Encapsulation

- Modify the `Product` class.
- Make `price` a private attribute (`__price`).
- Implement getter and setter methods:
  - `get_price()` – Returns the product price.
  - `set_price(new_price)` – Updates the price only if it is greater than zero.
- Test price modification using the setter.

### Task 3: Inheritance (Single-Level)
**Concept:** Inheritance and Method Overriding

- Create an `ElectronicProduct` subclass that inherits from `Product`.
- Additional attribute: `warranty_years`.
- Override the `get_info()` method to include warranty information.
- Create an object and demonstrate inheritance and method overriding.

### Task 4: Polymorphism
**Concept:** Runtime Polymorphism

- Create two classes:
  - `Laptop(Product)`
  - `Mobile(Product)`
- Override the `get_info()` method in both classes.
- Display product details in their own style.
- Use a loop to iterate over Laptop and Mobile objects and call `get_info()`.

### Task 5: Abstraction (Using Abstract Base Class)
**Concept:** Abstraction and Abstract Methods

- Create an abstract class `Payment`.
- Define the abstract method `process_payment(amount)`.
- Create two subclasses:
  - `CreditCardPayment`
  - `UPIPayment`
- Override `process_payment()` in both subclasses.
- Test all classes.

### Task 6: Magic Methods & Operator Overloading
**Concept:** Magic Methods and Operator Overloading

Add the following methods to the `Product` class:

**1. `__str__()`**
- Returns a readable string representation of a product.
- Includes product name, price, and category.

**2. `__add__()`**
- Overloads the `+` operator.
- Allows two Product objects to be added.
- Returns the total combined price.

Example:
```python
product1 + product2
```

### Task 7: Mini Project – Simple Inventory System
**Concept:** Classes, Objects, Composition, and Operator Overloading

Create the following classes:

**1. Inventory**

Attributes:
- `products` – A list to store Product objects.

Methods:
- `add_product(product)` – Adds a product.
- `remove_product(name)` – Removes a product by name.
- `get_total_value()` – Calculates the sum of all product prices.
- `show_all_products()` – Displays information about all products.

**2. Store**

Attributes:
- `store_name`
- `inventory` – An Inventory object.

Methods:
- `add_new_product()` – Takes user input and creates a Product object.
- `show_summary()` – Displays the total number of items and total inventory value.

**Testing Requirements:**
1. Create a Store object.
2. Add three products.
3. Display the inventory summary.
4. Use `__add__()` to combine the prices of two products.

---

## OOP Concepts Covered

| Concept | Description |
|---|---|
| Class | Blueprint for creating objects |
| Object | Instance of a class |
| Constructor | Initializes object attributes using `__init__()` |
| Encapsulation | Restricts direct access to data |
| Inheritance | Allows one class to inherit another class's properties |
| Polymorphism | Allows methods to behave differently in different classes |
| Abstraction | Hides implementation details and defines essential methods |
| Method Overriding | Redefines a parent class method in a child class |
| Magic Methods | Special methods such as `__str__()` and `__add__()` |
| Operator Overloading | Defines custom behavior for operators |
| Composition | Builds a class using objects of another class |

---

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code or another Python IDE.
3. Ensure Python 3 is installed.
4. Open the Python file containing the required task.
5. Run the program:

```bash
python filename.py
```

---

## Learning Outcomes

After completing these tasks, the following concepts can be understood and implemented:

- Creating and working with Python classes and objects.
- Understanding constructors and encapsulation.
- Implementing inheritance and polymorphism.
- Using abstract classes and abstract methods.
- Working with magic methods and operator overloading.
- Developing a simple inventory management system using OOP principles.

