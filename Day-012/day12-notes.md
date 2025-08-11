# 🔪 Day 12 - String Slicing & Operations on Strings

## 📏 Length of a String

* Use the `len()` function to get the length of a string.

```python
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
```

**Output:**

```
Mango is a 5 letter word.
```

---

## 🧩 String as an Array

* Strings are sequences (arrays) of characters.
* You can access specific characters using their index (0-based).

```python
pie = "ApplePie"
print(pie[:5])     # First 5 characters
print(pie[6])      # Character at index 6
```

**Output:**

```
Apple
i
```

> **Note:** Selecting a part of a string using indexes is called **slicing**.

---

## ✂️ Slicing Examples

```python
pie = "ApplePie"
print(pie[:5])      # Slicing from start
print(pie[5:])      # Slicing till end
print(pie[2:6])     # Slicing in between
print(pie[-8:])     # Slicing using negative index
```

**Output:**

```
Apple
Pie
pleP
ApplePie
```

---

## 🔄 Looping Through a String

* Strings are iterable.
* You can loop through each character using a `for` loop.

```python
alphabets = "ABCDE"
for i in alphabets:
    print(i)
```

**Output:**

```
A
B
C
D
E
```

---

✅ That wraps up **Day 12**! I’ve learned how to measure string length, treat strings as arrays, slice them in different ways, and loop through them.
