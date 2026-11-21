# Streamlit Mini Projects

## 📌 Projects Included

### 1. Basic Streamlit App 
- Displays a welcome title.
- Takes the user's name using a text input.
- Displays a personalized greeting when the user clicks the **Greet Me** button.

**Streamlit Components:**
- `st.title()`
- `st.text_input()`
- `st.button()`
- `st.write()`

### 2. Price Calculator 
- Takes the original product price.
- Allows users to select a discount percentage using a slider (0–50%).
- Calculates the discounted price.
- Displays the final price using a success message.
- Shows a before-and-after price comparison table.

**Streamlit Components:**
- `st.number_input()`
- `st.slider()`
- `st.button()`
- `st.success()`
- `st.table()`

### 3. Product Form 
- Takes product details through the Streamlit sidebar.
- Accepts product name and price.
- Provides a category selection dropdown.
- Displays a success message after adding a product.
- Shows product details in a clean tabular format.

**Streamlit Components:**
- `st.sidebar.text_input()`
- `st.sidebar.selectbox()`
- `st.sidebar.number_input()`
- `st.sidebar.button()`
- `st.success()`
- `st.table()`

### 4. Mini Dashboard 
- Displays a Simple Sales Dashboard.
- Provides a dropdown to select a month.
- Stores monthly sales in a Python dictionary.
- Displays selected month's sales using a metric.
- Visualizes monthly sales using a bar chart.

**Streamlit Components:**
- `st.title()`
- `st.write()`
- `st.selectbox()`
- `st.metric()`
- `st.bar_chart()`

## 🛠️ Technologies Used

- Python
- Streamlit

## 📂 Project Structure

```text
Streamlit-Mini-Projects/
│
├── Task1.py
├── Task2.py
├── Task3.py
├── Task4.py
│
└── README.md
```

## ⚙️ Installation

**Step 1: Install Python**

Make sure Python is installed on your system.

**Step 2: Install Streamlit**

Open the terminal and execute:

```bash
pip install streamlit
```

**Step 3: Clone the Repository**

```bash
git clone <your-repository-url>
```

**Step 4: Navigate to the Project Folder**

```bash
cd Streamlit-Mini-Projects
```

## ▶️ How to Run

Run each application separately using the following commands:

**Task 1 – Basic Streamlit App**
```bash
streamlit run Task1.py
```

**Task 2 – Price Calculator**
```bash
streamlit run Task2.py
```

**Task 3 – Product Form**
```bash
streamlit run Task3.py
```

**Task 4 – Mini Dashboard**
```bash
streamlit run Task4.py
```

Streamlit will start a local development server and open the application in your web browser.

## 🎯 Learning Outcomes

Through these projects, I learned:

- Creating interactive web applications using Streamlit.
- Taking user input through different UI components.
- Using buttons, sliders, and dropdown menus.
- Performing calculations using Python.
- Working with Python lists and dictionaries.
- Creating forms using Streamlit's sidebar.
- Displaying data using tables and metrics.
- Visualizing data using bar charts.
