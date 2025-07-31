# Day 3 - Modules and pip in Python

## What is a Module?
A **module** is like a code library which can be used to borrow code written by somebody else in our Python program.

There are two types of modules in Python:

### 1. Built-in Modules
- These come pre-installed with Python.
- No need to install them explicitly.
- Examples: `math`, `random`, `datetime`, `os`

#### Example: Using a built-in module
```python
import math
print(math.sqrt(25))  # Output: 5.0
```

### 2. External Modules
- These are written by other developers and not included with Python by default.
- You need to install them using a package manager like `pip`.
- Examples: `pandas`, `numpy`, `flask`, `requests`

## The `pip` command
`pip` is used as a package manager to install external Python modules.

### Installing a module:
```bash
pip install pandas
```

## Using a Module in Python
We use the `import` keyword to bring a module into our program.

### Example: Using an external module
```python
import pandas as pd

# Read and work with a file named 'words.csv'
df = pd.read_csv('words.csv')
print(df)  # This will display the contents of the words.csv file
```

You can install and explore other modules and look into their documentation for usage instructions.

**Note:** We’ll be doing this often in the later part of this course.
