# 🍬 Functional Treat

## Python Data Analyzer and Transformer

**Functional Treat** is a beginner-friendly Python program that demonstrates different types of Python functions and list operations.

The program allows users to enter data and perform different analysis and transformation operations using a simple menu-driven interface.

---

## 📌 Project Description

The **Functional Treat** project is a Data Analyzer and Transformer program developed in Python.

The project demonstrates the use of:

- Built-in functions
- User-defined functions (UDF)
- `*args`
- `**kwargs`
- `__doc__`
- Recursion
- Lambda functions
- `global` keyword
- Returning multiple values
- 1D and 2D lists
- Sorting list data
- `map()` and `filter()`

The main purpose of this project is to understand how different Python functions can be used to analyze and transform data.

---

## 🎯 Objective

The objective of this project is to create a menu-driven Python program that allows users to:

- Enter dataset values
- Analyze the dataset
- Calculate basic statistics
- Filter data
- Sort data
- Calculate factorial using recursion
- Work with 1D and 2D lists
- Demonstrate different Python function concepts

---

## ✨ Features

### 1. 📥 Input Data

The user can enter a 1D list of numbers.

Example:

```text
34 12 56 78 43 21 90
```

The data is stored in a Python list.

The program can also work with 2D lists (nested lists).

Example:

```python
data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

---

### 2. 📊 Built-in Functions

The program demonstrates Python built-in functions such as:

```python
len()
sum()
min()
max()
```

These functions are used to display basic statistics of the dataset.

Example:

```text
Total elements: 7
Minimum value: 12
Maximum value: 90
Sum of all values: 334
Average value: 47.71
```

---

### 3. 🧑‍💻 User-Defined Functions

The project uses user-defined functions to perform different operations.

Example:

```python
def calculate_average(data):
    return sum(data) / len(data)
```

Functions make the program easier to understand and organize.

---

### 4. 📦 `*args`

The project demonstrates the use of `*args` to accept multiple values.

Example:

```python
def show_values(*args):
    for value in args:
        print(value)
```

---

### 5. 🔑 `**kwargs`

The project demonstrates the use of `**kwargs` to accept multiple key-value pairs.

Example:

```python
def dataset_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
```

---

### 6. 📖 `__doc__`

The project uses `__doc__` to provide documentation for functions.

Example:

```python
def calculate_average(data):
    """Calculate the average of the dataset."""
    return sum(data) / len(data)
```

The documentation can be displayed using:

```python
print(calculate_average.__doc__)
```

---

### 7. 🔄 Recursion

The program demonstrates recursion using factorial calculation.

Example:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

Example:

```text
Enter a number to calculate its factorial: 5

Factorial of 5 is: 120
```

---

### 8. λ Lambda Function

Lambda functions are used to filter data based on a user-defined threshold.

Example:

```python
result = list(filter(lambda x: x >= threshold, data))
```

Example:

```text
Enter threshold: 50

Filtered Data:
56, 78, 90
```

---

### 9. 🌐 Global Keyword

The project demonstrates the use of the `global` keyword.

Example:

```python
total_values = 0

def update_total(data):
    global total_values
    total_values = len(data)
```

The global variable can be accessed by different functions.

---

### 10. 🔙 Returning Multiple Values

The program demonstrates how a function can return multiple values.

Example:

```python
def dataset_statistics(data):
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / len(data)

    return minimum, maximum, total, average
```

The values can be received separately:

```python
minimum, maximum, total, average = dataset_statistics(data)
```

---

### 11. 📋 1D and 2D Lists

The project demonstrates both 1D and 2D lists.

#### 1D List

```python
data = [34, 12, 56, 78, 43, 21, 90]
```

#### 2D List

```python
data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

A 2D list can be displayed as:

```text
10  20  30
40  50  60
70  80  90
```

---

### 12. 🔃 Sorting Data

The project demonstrates sorting using `sort()` and `sorted()`.

#### Ascending Order

```python
data.sort()
```

Example output:

```text
12, 21, 34, 43, 56, 78, 90
```

#### Descending Order

```python
data.sort(reverse=True)
```

Example output:

```text
90, 78, 56, 43, 34, 21, 12
```

The project also demonstrates the difference between `sort()` and `sorted()`.

---

## 🖥️ Main Menu

The program provides a simple menu-driven interface:

```text
Welcome to the Data Analyzer and Transformer Program

Main Menu:

1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program

Please enter your choice:
```

---

## 📊 Example Output

### Input Data

```text
Enter data for a 1D array (separated by spaces):

34 12 56 78 43 21 90

Data has been stored successfully!
```

### Data Summary

```text
Data Summary:

- Total elements: 7
- Minimum value: 12
- Maximum value: 90
- Sum of all values: 334
- Average value: 47.71
```

### Factorial

```text
Enter a number to calculate its factorial: 5

Factorial of 5 is: 120
```

### Filtering

```text
Enter a threshold value: 50

Filtered Data:
56, 78, 90
```

### Sorting

```text
Sorted Data in Ascending Order:

12, 21, 34, 43, 56, 78, 90
```

### Dataset Statistics

```text
Dataset Statistics:

- Minimum value: 12
- Maximum value: 90
- Sum of values: 334
- Average value: 47.71
```

---

## 🛠️ Technologies Used

- **Python 3**
- **Python IDLE**
- **Lists**
- **Functions**
- **Lambda Functions**
- **Recursion**
- **Built-in Functions**

---

## 📚 Concepts Used

| Concept | Purpose |
|---|---|
| `len()` | Count elements |
| `sum()` | Calculate total |
| `min()` | Find minimum value |
| `max()` | Find maximum value |
| UDF | Create custom functions |
| `*args` | Accept multiple arguments |
| `**kwargs` | Accept key-value arguments |
| `__doc__` | Function documentation |
| Recursion | Factorial calculation |
| Lambda | Filtering data |
| `filter()` | Filter list values |
| `map()` | Transform list values |
| `global` | Access global variables |
| Multiple return values | Return multiple statistics |
| 1D List | Store simple data |
| 2D List | Store nested data |
| `sort()` | Sort original list |
| `sorted()` | Return a sorted list |

---

## 📁 Project Structure

```text
Functional-Treat/
│
├── functional_treat.py
│
└── README.md
```

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the installation:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone YOUR-GITHUB-REPOSITORY-LINK
```

### Step 3: Open the Project Folder

```bash
cd Functional-Treat
```

### Step 4: Run the Program

```bash
python functional_treat.py
```

You can also open the `.py` file using **Python IDLE** and select:

```text
Run → Run Module
```

---

## 🎥 Project Demonstration Video

### ▶️ Video Link

**https://drive.google.com/file/d/1BICNcjcrAIxhh39lQwn2uRW7zfWG-6Pp/view?usp=drive_link**

## 🎓 Learning Outcomes

After completing this project, I learned:

- How to create Python functions
- How to use built-in functions
- How to create user-defined functions
- How `*args` and `**kwargs` work
- How to use `__doc__`
- How recursion works
- How lambda functions work
- How `map()` and `filter()` work
- How to use the `global` keyword
- How to return multiple values
- How to work with 1D and 2D lists
- How to sort list data
- How to create a menu-driven Python program

---

## 👨‍💻 Author

**HARSH PRAJAPATI**

**Project Name:** Functional Treat  
**Language:** Python 3  
**Project Type:** Data Analyzer and Transformer

---

## ⭐ Conclusion

**Functional Treat** is a simple educational Python project that combines different Python function concepts with list-based data analysis and transformation.

The project provides practical experience with **functions, recursion, lambda expressions, lists, sorting, filtering, and data analysis** through a simple menu-driven program.

---

## 📜 License

This project is created for **educational and academic purposes**.
