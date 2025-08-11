# 📅 Day 13 - String Methods in Python

Python provides a set of built-in methods that allow you to alter, analyze, and manipulate strings.

---

## 1. **`upper()`**

Converts all characters to uppercase.

```python
str1 = "AbcDEfghIJ"
print(str1.upper())   # True case
print("abc".upper())  # Also works on lowercase only
```

**Output:**

```
ABCDEFGHIJ
ABC
```

---

## 2. **`lower()`**

Converts all characters to lowercase.

```python
str1 = "AbcDEfghIJ"
print(str1.lower())   # True case
print("ABC".lower())  # Works on uppercase only
```

**Output:**

```
abcdefghij
abc
```

---

## 3. **`strip()`**

Removes whitespace before and after the string.

```python
str2 = "  Silver Spoon  "
print(str2.strip())     # True case
print("NoSpace".strip()) # No spaces to remove
```

**Output:**

```
Silver Spoon
NoSpace
```

---

## 4. **`rstrip(chars)`**

Removes trailing characters.

```python
str3 = "Hello !!!"
print(str3.rstrip("!")) # True case
print("Hello".rstrip("!")) # No exclamation marks to remove
```

**Output:**

```
Hello
Hello
```

---

## 5. **`replace(old, new)`**

Replaces all occurrences of a substring with another.

```python
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))   # True case
print(str2.replace("Z", "M"))    # No match
```

**Output:**

```
Silver Moon
Silver Spoon
```

---

## 6. **`split(delimiter)`**

Splits a string into a list.

```python
str2 = "Silver Spoon"
print(str2.split(" "))   # True case
print(str2.split(","))   # No comma found
```

**Output:**

```
['Silver', 'Spoon']
['Silver Spoon']
```

---

## 7. **`capitalize()`**

Capitalizes first character, rest lowercase.

```python
str1 = "hello"
print(str1.capitalize())  # True case
print("HELLO".capitalize()) # Already uppercase
```

**Output:**

```
Hello
Hello
```

---

## 8. **`center(width, char)`**

Centers string with optional padding.

```python
str1 = "Welcome"
print(str1.center(20))       # True case
print(str1.center(20, '.'))  # With padding character
```

**Output:**

```
      Welcome       
.......Welcome.......
```

---

## 9. **`count(substring)`**

Counts occurrences of substring.

```python
str2 = "Abracadabra"
print(str2.count("a"))  # True case
print(str2.count("z"))  # False case
```

**Output:**

```
4
0
```

---

## 10. **`endswith(suffix)`**

Checks if string ends with given suffix.

```python
str1 = "Welcome!!!"
print(str1.endswith("!!!"))  # True
print(str1.endswith("?"))    # False
```

**Output:**

```
True
False
```

---

## 11. **`find(substring)`**

Finds index of first occurrence, returns `-1` if not found.

```python
str1 = "Hello World"
print(str1.find("World"))  # True case
print(str1.find("Python")) # False case
```

**Output:**

```
6
-1
```

---

## 12. **`index(substring)`**

Like `find()` but raises error if not found.

```python
str1 = "Hello World"
print(str1.index("World"))  # True case
# print(str1.index("Python")) # False case - will raise ValueError
```

**Output:**

```
6
```

---

## 13. **`isalnum()`**

Returns True if only letters/numbers.

```python
print("Python3".isalnum())  # True
print("Python 3".isalnum()) # False
```

**Output:**

```
True
False
```

---

## 14. **`isalpha()`**

Returns True if only letters.

```python
print("Python".isalpha())  # True
print("Python3".isalpha()) # False
```

**Output:**

```
True
False
```

---

## 15. **`islower()`**

Checks if all lowercase.

```python
print("python".islower()) # True
print("Python".islower()) # False
```

**Output:**

```
True
False
```

---

## 16. **`isprintable()`**

Checks if all characters are printable.

```python
print("Hello".isprintable())   # True
print("Hello\n".isprintable()) # False
```

**Output:**

```
True
False
```

---

## 17. **`isspace()`**

Checks if only whitespace.

```python
print("   ".isspace()) # True
print(" a ".isspace()) # False
```

**Output:**

```
True
False
```

---

## 18. **`istitle()`**

Checks if title-cased.

```python
print("Hello World".istitle()) # True
print("Hello world".istitle()) # False
```

**Output:**

```
True
False
```

---

## 19. **`isupper()`**

Checks if all uppercase.

```python
print("HELLO".isupper()) # True
print("Hello".isupper()) # False
```

**Output:**

```
True
False
```

---

## 20. **`startswith(prefix)`**

Checks if string starts with prefix.

```python
print("Python".startswith("Py")) # True
print("Python".startswith("py")) # False
```

**Output:**

```
True
False
```

---

## 21. **`swapcase()`**

Swaps uppercase to lowercase and vice versa.

```python
print("Hello".swapcase())  # True case
print("hELLO".swapcase())  # Mixed case
```

**Output:**

```
hELLO
Hello
```

---

## 22. **`title()`**

Capitalizes first letter of each word.

```python
print("hello world".title()) # True case
print("HELLO WORLD".title()) # Already uppercase
```

**Output:**

```
Hello World
Hello World
```

---

✅ That wraps up **Day 13**! I’ve learned how to use Python string methods effectively with both **true** and **false** cases.
