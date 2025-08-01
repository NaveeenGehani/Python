# 🐍 Day 6 - Variables and Data Types in Python

## 🔹 What is a Variable?

* A **variable** is like a container that holds data in memory.
* Think of it like a jar that stores sugar or salt in a kitchen.
* Assigning a value to a variable in Python is simple:

```python
a = 1
b = True
c = "Harry"
d = None
```

* These are four variables holding different **data types**.

---

## 🔹 What is a Data Type?

* **Data Type** specifies what kind of value a variable holds.
* Helps avoid errors during operations and ensures correct behavior.
* You can check a variable's type using `type()`:

```python
a = 1
print(type(a))        # <class 'int'>

b = "1"
print(type(b))        # <class 'str'>
```

---

## 📚 Built-in Data Types in Python

### 1. **Numeric Data**: `int`, `float`, `complex`

* `int`: Whole numbers → `3`, `-8`, `0`
* `float`: Decimal numbers → `7.349`, `-9.0`, `0.0000001`
* `complex`: Complex numbers → `6 + 2j`

---

### 2. **Text Data**: `str`

* A string of characters surrounded by quotes.

```python
name = "Hello World!!!"
print(type(name))  # <class 'str'>
```

---

### 3. **Boolean Data**: `bool`

* Either `True` or `False`.

```python
is_active = True
print(type(is_active))  # <class 'bool'>
```

---

### 4. **Sequenced Data**: `list`, `tuple`

#### ✅ List

* Ordered, mutable collection.
* Enclosed in square brackets `[]`.

```python
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
# Output: [8, 2.3, [-4, 5], ['apple', 'banana']]
```

#### ✅ Tuple

* Ordered, immutable collection.
* Enclosed in parentheses `()`.

```python
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
# Output: (("parrot", "sparrow"), ("Lion", "Tiger"))
```

---

### 5. **Mapped Data**: `dict`

* Unordered collection of key-value pairs.
* Enclosed in curly braces `{}`.

```python
dict1 = {"name": "Sakshi", "age": 20, "canVote": True}
print(dict1)
# Output: {'name': 'Sakshi', 'age': 20, 'canVote': True}
```

---

✅ That wraps up **Day 6**! I now understood how variables and data types work in Python. Keep going strong!
