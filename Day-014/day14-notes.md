# 📅 Day 14 - Conditional Statements in Python

Conditional statements let you execute different blocks of code depending on whether a condition evaluates to **True** or **False**.



---
## Conditional Operators
Conditional operators (also known as comparison operators) are used to compare two values. The result of a comparison is either `True` or `False`.

| Operator | Name                     | Example        | Result  |
|----------|--------------------------|----------------|---------|
| `==`     | Equal to                 | `5 == 5`       | True    |
| `!=`     | Not equal to             | `5 != 3`       | True    |
| `>`      | Greater than             | `7 > 3`        | True    |
| `<`      | Less than                | `2 < 5`        | True    |
| `>=`     | Greater than or equal to | `4 >= 4`       | True    |
| `<=`     | Less than or equal to    | `3 <= 8`       | True    |

These operators are used to compare values and determine the truth value of expressions.

---


## Types of Conditional Statements

1. `if`
2. `if-else`
3. `if-elif-else`
4. Nested `if-else`

---

## **if-else Statement**

**Working:**

* If the condition is `True`: execute the `if` block.
* If the condition is `False`: execute the `else` block.

```python
applePrice = 210
budget = 200

if applePrice <= budget:
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
```

**Output:**

```
Alexa, do not add Apples to the cart.
```

---

## **elif Statement**

Used when multiple conditions need to be checked.

```python
num = 0
if num < 0:
    print("Number is negative.")
elif num == 0:
    print("Number is Zero.")
else:
    print("Number is positive.")
```

**Output:**

```
Number is Zero.
```

---

## **Nested if Statements**

You can place one `if` (or `if-else`) inside another.

```python
num = 18
if num < 0:
    print("Number is negative.")
elif num > 0:
    if num <= 10:
        print("Number is between 1-10")
    elif num > 10 and num <= 20:
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
```

**Output:**

```
Number is between 11-20
```

---

✅ That wraps up **Day 14** — I’ve learned how to use `if`, `elif`, `else`, and nested conditionals to control program flow.
