# 🐍 Day 9 - Typecasting in Python

## 🔹 What is Typecasting?

* Typecasting (or type conversion) is the process of converting one data type into another.
* Python supports several built-in functions for typecasting, including:

  * `int()`
  * `float()`
  * `str()`
  * `ord()`
  * `hex()`
  * `oct()`
  * `tuple()`
  * `set()`
  * `list()`
  * `dict()`

---

## 🔸 Types of Typecasting

### ✅ Explicit Typecasting

* Performed manually by the programmer.
* Uses built-in functions.
* Syntax: `new_data_type(value)`

#### Example:

```python
string = "15"
number = 7
string_number = int(string)  # Converts string to integer
sum = number + string_number
print("The Sum of both the numbers is:", sum)
```

**Output:**

```
The Sum of both the numbers is: 22
```

---

### 🔄 Implicit Typecasting

* Performed automatically by Python.
* Python converts a lower data type to a higher one to prevent data loss.

#### Example:

```python
a = 7
print(type(a))  # <class 'int'>

b = 3.0
print(type(b))  # <class 'float'>

c = a + b
print(c)        # 10.0
print(type(c))  # <class 'float'>
```

**Output:**

```
<class 'int'>
<class 'float'>
10.0
<class 'float'>
```

---

✅ That’s all for **Day 9**! I’ve now learned both implicit and explicit type conversion in Python.
