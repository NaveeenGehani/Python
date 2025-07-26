# 📅 Day 2: Taking User Input

## 🔍 What I Learned
- The `input()` function allows interaction with the user by collecting input from the keyboard.
- Variables are used to store the values received from `input()`.
- Variables cannot have spaces or start with a number.
- Variable naming conventions include:
  - `snake_case` (e.g., `user_name`)
  - `camelCase` (e.g., `userName`)
- Common errors include syntax issues, misnamed variables, and printing literal strings instead of variable values.

---

## 🧠 Examples and Concepts

### ✅ Basic Input
```python
input("What is Your Name?: ")
```
**Explanation:** Displays a prompt and waits for the user to type something and press Enter.

---

### ✅ Storing Input in a Variable
```python
userName = input("What is Your Age?: ")
print("Your name is ")
print(userName)
```
**Explanation:** The user's input is stored in `userName`. To use it later, just refer to the variable name.

---

### ✅ Multiple Inputs and Outputs
```python
myName = input("What's your name? ")
myAge = input("How old are you? ")
replit = input("Do you like Replit? ")

print("Gee, that's REALLY OLD")

print()
print("So, you are")
print(myName)
print("and are the ripe old age of")
print(myAge)
print("and clearly think that Replit is")
print(replit)
```

---

## ❌ Common Mistakes and Fixes

### 1. Syntax Error (Invalid Variable Name)
```python
# my variable = input("WHO GOES THERE? ") ❌
# print(my variable)

my_variable = input("WHO GOES THERE? ")  # ✅
print(my_variable)
```

### 2. Name Error (Case Sensitivity)
```python
# myGrandma = input("How's your Grandma doing? 😘 ")
# print(mygrandma)  # ❌

myGrandma = input("How's your Grandma doing? 😘 ")
print(myGrandma)  # ✅
```

### 3. Literal String Mistake
```python
myLunch = input("What are you having for lunch? ")
print("Hmm, it sounds like you really should just order")
# print("myLunch")  # ❌ prints the word "myLunch"
print(myLunch)    # ✅ prints the value stored in myLunch
print("as soon as possible!")
```

### 4. Syntax Error: Missing Equal Sign
```python
# maidenName input("What is your Mother's maiden name? ") ❌

maidenName = input("What is your Mother's maiden name? ")  # ✅
print(maidenName)
```

---

## 🤔 What I Found Tricky
- Forgetting to assign a variable with `=` before calling `input()`.
- Printing a variable name as a string (in quotes) instead of the actual value.
- Case sensitivity in variable names caused unexpected errors.

---

## 🌱 Extra Practice
- Ask the user about their favorite food, color, or hobby.
- Create a "fake login" screen that collects name, email, and password (just for fun, not security!).
