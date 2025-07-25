# 🐍 Day 1: Printing in Python

## 🔍 What I Learned
- `print()` is the function used to display text on the screen in Python.
- Text (strings) must be enclosed in quotes — either `'single'` or `"double"`.
- Triple quotes (`"""..."""` or `'''...'''`) allow multi-line strings.
- Python is **case-sensitive** — `Print()` is not the same as `print()`.
- Common beginner errors involve syntax: missing parentheses, quotes, or capitalization.

---

## 🧠 Notes and Examples

### ✅ Basic Printing
```python
print("Hello World!")
```

### ✅ Printing Multiple Lines with Separate Statements
```python
print("Well we")
print("just use more lines")
print("of code")
```

### ✅ Printing Multi-line String using Triple Quotes
```python
print("""Well we
just use more lines
of code""")
```

```python
print("""Anything that starts
with three quotes, and ends
in three quotes can span
many lines and even contain " symbols
within it without freaking anything out!""")
```

---

## ❌ Common Mistakes and Fixes

### 1. Capitalization Error
```python
# Print("What could go wrong?") ❌
print("What could go wrong?") ✅
```
**Explanation:** `Print()` with a capital 'P' is invalid. Python is case-sensitive.

---

### 2. Missing Parentheses (Python 2-style)
```python
# print "Hello Again" ❌
print("Hello Again") ✅
```
**Explanation:** In Python 3, `print` is a function and requires parentheses.

---

### 3. Missing Quotes Around Strings
```python
# print(Please work) ❌
print("Please work") ✅

# print(= MUSIC+ =) ❌
print("= MUSIC+ =") ✅
```
**Explanation:** Strings must be enclosed in quotes. Otherwise, Python treats them as variables or invalid expressions.

---

### 4. Unbalanced or Missing Quotes
```python
# print("> Songs" ❌
print("> Songs") ✅

# Print("> Albums") ❌
print("> Albums") ✅

# print(> Artists") ❌
print("> Artists") ✅
```
**Explanation:** Make sure every opening quote has a matching closing quote, and don’t forget that `print` must be lowercase.

---

## 🤔 What I Found Tricky
- Forgetting that Python is case-sensitive.
- Triple quotes were new and felt unusual at first, but helpful.
- Realized most errors are just typos or formatting issues.

---

## 🌱 Extra Practice
Try printing:
- A grocery list using multi-line string syntax.
- A short poem using both separate print statements and triple quotes.
