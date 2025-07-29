# Day 5: If-Else Statements

## What I Learned
- The `if` statement checks if a condition is true.
- The `else` block runs when the `if` condition is not met.
- Use `==` to compare values, not `=` (which is for assignment).
- Python uses **indentation** (spaces or tabs) to define blocks of code.

---

## Examples

### Basic `if` Statement
```python
myName = input("What's your name?: ")
if myName == "Naveen":
    print("Welcome Naveen!")
```

### `if-else` Statement
```python
myName = input("What's your name?: ")
if myName == "Naveen":
    print("Welcome Naveen!")
    print("How are you Naveen?")
else:
    print("Who on earth are you?!")
```

---

## Common Errors

### 1. Using `=` instead of `==`
```python
# if catsOrDogs = "cat": ❌ (assignment instead of comparison)
if catsOrDogs == "cat":  # ✅
    print("Meow")
else:
    print("Woof")
```

### 2. Indentation Error
```python
# else:
# print("Woof") ❌ (not indented)

else:
    print("Woof")  # ✅
```

---

## Practice Ideas
- Ask the user their favorite animal and print a custom response.
- Create a simple login where only your name gets a special greeting.
