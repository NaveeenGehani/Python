# Day 4: Adding Color to Console Text

## What I Learned
- You can change the color of terminal text using **ANSI escape codes**.
- Format: `\033[{color-code}mYour text\033[0m`
- `\033[` starts the escape sequence.
- `{color-code}` is a number from the list below that tells the terminal which color to use.
- `\033[0m` resets the text color back to default.

---

## Color Codes Table
| Color Name | Code |
|------------|------|
| Default    | 0    |
| Black      | 30   |
| Red        | 31   |
| Green      | 32   |
| Yellow     | 33   |
| Blue       | 34   |
| Purple     | 35   |
| Cyan       | 36   |
| White      | 37   |

---

## Example
```python
print("\033[31mThis text is red\033[0m")
```

**Explanation:**
- `\033[31m` makes the text red.
- `\033[0m` resets the color so the rest of the output isn't red.

---

## Practice Ideas
- Print your name in different colors.
- Combine user input with colored text.
- Make a mini "alert system" that prints warnings in red, success in green, etc.
