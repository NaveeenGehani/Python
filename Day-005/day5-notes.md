# 🚀 Day 5 - Comments, Escape Sequences & Print in Python

Welcome to **Day 5** of #100DaysOfCode. Today’s topics include:

- Python Comments (Single-line & Multi-line)
- Escape Sequence Characters
- Additional Parameters in `print()` statement

---

## 📝 Python Comments

### ➤ What are Comments?
- Comments are notes in your code ignored by the Python interpreter.
- They help explain logic or disable lines temporarily during testing.

---

### ➤ Single-Line Comments
- Use `#` to write a single-line comment.

```python
# This is a 'Single-Line Comment'
print("This is a print statement.")  # Output: This is a print statement.

print("Hello World !!!")  # Printing Hello World
# Output: Hello World !!!

print("Python Program")
# print("Python Program")  # This line won't execute
# Output: Python Program
```

---

### ➤ Multi-Line Comments

✅ Two ways to write multi-line comments:

1. Use `#` on each line.
2. Use triple quotes `""" ... """` or `''' ... '''`.

```python
# It will execute a block of code if a specified condition is true.
# If the condition is false then it will execute another block of code.
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
# Output: p is greater than 5.
```

```python
"""This is an if-else statement.
It will execute a block of code if a specified condition is true.
If the condition is false then it will execute another block of code."""
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
# Output: p is greater than 5.
```

---

## 🔡 Escape Sequence Characters

- Used to insert characters that can’t be typed directly in a string.
- Starts with a backslash (`\`), followed by a character.

```python
print("This doesn't "execute")        # ❌ Error
print("This will \"execute\"")        # ✅ Output: This will "execute"
```

Common Escape Sequences:

| Escape | Description        |
|--------|--------------------|
| \n     | New Line           |
| \t     | Tab Space          |
| \"     | Double Quote       |
| \'     | Single Quote       |
| \\     | Backslash          |

---

## 🖨️ More on `print()` Statement

### ➤ Syntax

```python
print(object(s), sep=separator, end=end, file=file, flush=flush)
```

### ➤ Parameters

- `object(s)`: One or more values to print.
- `sep`: Separator between objects (default is `' '`).
- `end`: String appended after the last object (default is `'\n'`).
- `file`: Output destination (default is `sys.stdout`).
- `flush`: Whether to flush the output buffer (default is `False`).

### ➤ Examples

```python
print("Hello", "World")                   # Output: Hello World
print("Hello", "World", sep="-")         # Output: Hello-World
print("Hello", end=" ")                  
print("World")                           # Output: Hello World
```

---

