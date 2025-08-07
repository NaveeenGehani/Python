# 📚 Day 11 – Strings in Python

## 🔤 What are Strings?
- In Python, anything enclosed between **single** (`' '`) or **double** (`" "`) quotation marks is considered a **string**.
- A string is a **sequence of characters**, often used to represent textual data (Unicode).

---

## ✨ Example:
```python
name = "Naveen"
print("Hello, " + name)
```

### 🖥️ Output:
```
Hello, Naveen
```

✅ It doesn't matter if you use single or double quotes — the result will be the same.

---

## 🗨️ Quotes Inside Strings
To include quotation marks inside a string, you can:
- Use different types of quotes
- Or use **escape characters** (`\"`)

```python
print('He said, "I want to eat an apple".')

name = "Naveen \"is a good programmer\""
print(name)

```

---

## 📝 Multiline Strings
Use triple quotes (`'''` or `"""`) for multiline strings:

```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

---

## 🎯 Accessing Characters of a String
- Strings are like arrays (or lists) of characters.
- You can access a character by its **index** (starting from 0):

```python
print(name[0])  # First character
print(name[1])  # Second character
```

---

## 🔁 Looping Through a String
You can loop through a string using a `for` loop:

```python
for character in name:
    print(character)
```

➡️ This will print each character in the string one by one.

---

✅ That wraps up **Day 11**! I've learned how to define, access, and work with strings in Python.
