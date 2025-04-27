# 🚀 Lesson 3 — **Mastering Conditionals in Python**

---

## 🧠 1. What are Conditionals?

Conditionals allow your program to **decide** based on **True/False** evaluations.

**Simple idea:**
> If it rains, take an umbrella. Otherwise, enjoy the sun.

In Python:

```python
if raining:
    take_umbrella()
else:
    enjoy_sun()
```

---

## 🧩 2. Full Structure

```python
if condition:
    # do this
elif another_condition:
    # do that
else:
    # do something else
```

✅ Conditions must be **True** or **False**.  
✅ Always end `if`, `elif`, `else` lines with `:`.  
✅ Body must be **indented**.

---

## 🔥 3. Comparison Operators

| Operator | Meaning                | Example     |
|:---------|:------------------------|:------------|
| `==`     | Equal to                 | `a == b`    |
| `!=`     | Not equal to             | `a != b`    |
| `>`      | Greater than             | `a > b`     |
| `<`      | Less than                | `a < b`     |
| `>=`     | Greater than or equal to | `a >= b`    |
| `<=`     | Less than or equal to    | `a <= b`    |

---

## 🛠️ 4. Combining Conditions

Use **and**, **or**, **not**:

```python
if age > 18 and age < 30:
    print("Young adult")
    
if not raining:
    print("No umbrella needed")
```

---

# 🐍 5. Pythonic Way

Level up your code to be **cleaner, faster, and more readable**.

---

### ✨ One-Liner Conditionals (Ternary Operator)

✅ Super clean way to choose between two values:

```python
result = "Adult" if age >= 18 else "Minor"
```

Equivalent to:

```python
if age >= 18:
    result = "Adult"
else:
    result = "Minor"
```

---

### ✨ Clean Range Checking

Instead of writing:

```python
if age >= 18 and age <= 30:
```
Write:

```python
if 18 <= age <= 30:
```

✅ Reads like English!  
✅ **Preferred** style in Python.

---

### ✨ Avoid Redundant Conditions

Instead of:

```python
if is_sunny == True:
    enjoy_day()
```

Write:

```python
if is_sunny:
    enjoy_day()
```

✅ Let `True` values be checked **directly**.

---

## 🧪 6. Function Applications

---

### Example 1: Temperature Checker

```python
def check_temperature(temp):
    if temp > 30:
        return "Hot"
    elif 20 <= temp <= 30:
        return "Warm"
    elif 10 <= temp < 20:
        return "Cool"
    else:
        return "Cold"
```

✅ Notice **range checking** with `<=` and `<`.

---

### Example 2: Even or Odd (Pythonic One-Liner)

```python
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
```

---

### Example 3: Grading System (Proper Ranges)

```python
def get_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
        return "Invalid Score"
```

✅ Every possible score falls into exactly **one range**.  
✅ Also checks if the score is **valid**.

---

# 🆕 7. Python 3.10+: Structural Pattern Matching (`match/case`)

In Python 3.10 and above, we have a new, cleaner way to handle multiple options:  
**`match`** and **`case`** — similar to switch-case in other languages, but more powerful!

---

### Example: Weather Advisor

```python
def weather_advisor(weather):
    match weather:
        case "sunny":
            print("☀️ It's a sunny day!")
        case "rainy":
            print("🌧️ Bring an umbrella!")
        case "snowy":
            print("❄️ Wear a heavy coat!")
        case _:
            print("🌈 Weather unknown, enjoy your day!")

# Example usage
weather_advisor("rainy")
```

---

### Example: Grading Feedback

```python
def grade_feedback(grade):
    match grade:
        case "A":
            print("Excellent! 🎉")
        case "B":
            print("Good job! 👍")
        case "C":
            print("Keep pushing!")
        case "D":
            print("Needs improvement.")
        case "F":
            print("Don't give up!")
        case _:
            print("Invalid grade.")
```

---

### Quick Tips:

| Concept | Meaning |
|:--------|:--------|
| `match` | Start matching a value |
| `case`  | Each case to compare |
| `_`     | Wildcard (default case) |
| Bonus   | You can even match **patterns** like types, lists, dictionaries! (Advanced)

---

# ⚡ Quick Recap for Mastery:

| Topic | Core Idea |
|:------|:----------|
| `if / elif / else` | Control the flow based on truth tests |
| Comparison | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| Logical operators | `and`, `or`, `not` |
| Pythonic one-liner | `x if condition else y` |
| Clean Ranges | Use `<= value <=` for smooth checking |
| Direct Booleans | No need for `== True` or `== False` |
| Functions | Apply conditionals inside real functions |
| Python 3.10+ `match/case` | Elegant matching for multiple options |

---

# 🔥 Mini Challenges (Optional)

- Write a function `can_drive(age)` that returns `"Yes"` if age ≥ 18 else `"No"`.
- Write a function `describe_number(n)`:
  - `"Positive"` if >0
  - `"Negative"` if <0
  - `"Zero"` if =0
- Use `match/case` to build a **simple chatbot** that responds differently to "hello", "bye", "thanks", or anything else.
