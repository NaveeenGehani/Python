# Day 3: Concatenation

## What I Learned
- Concatenation means combining strings and variables together.
- The `print()` function allows multiple values to be printed using commas.
- Each part of the output (text or variable) should be separated by a comma inside `print()`.
- Variables should not be inside quotes, or they'll be treated as plain text.

---

## Examples

### Basic Concatenation
```python
myName = input("What's your name? ")
myLunch = input("What are you having for lunch? ")
print(myName, "is going to be chowing down on", myLunch, "very soon!")
```

**Explanation:**
- Each part (variable or string) is separated by commas.
- `print()` automatically adds spaces between each item.

---

## Common Errors

### Missing Commas
```python
yourName = input("Name: ")
whatYear = input("What year is it?: ")
# print(yourName "thinks it is" whatYear) ❌

print(yourName, "thinks it is", whatYear)  # ✅
```

### Variables Inside Quotes
```python
# print("yourName, thinks it is, whatYear") ❌ (prints literal string)
print(yourName, "thinks it is", whatYear)   # ✅ (prints values of variables)
```

---

## Practice Ideas
- Ask the user their name and favorite movie, then output a sentence using both.
- Make a short dialogue between two characters using user input and `print()`.
