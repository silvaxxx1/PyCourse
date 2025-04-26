# 🧠 Python Class Walkthrough — Lesson 2: Functions

Welcome back! After getting comfortable with variables, input/output, and basic math, it’s time to unlock one of the most powerful features in Python—**functions**. Functions allow you to organize your code, reduce repetition, and build complex operations easily.

Let's get started and dive into the magic of functions! 🎩✨

---

## 📘 Part 1: Why Functions?

### 🔹 **Reusability and Efficiency**
A function is a block of code that can be defined once and called many times with different inputs. This helps keep your code **DRY** (Don’t Repeat Yourself) and makes it easier to manage.

For example, instead of writing the same code multiple times:
```python
print("Hello Alice")
print("Hello Bob")
```
You can define a function and call it with different inputs:
```python
def greet(name):
    print(f"Hello, {name}!")

def main():
    greet("Alice")
    greet("Bob")

main()
```
Notice how we defined `greet()` once and used it multiple times. You’ll see the same concept applied to more complex tasks as we go along.

---

## ⚙️ Part 2: Defining Functions

### 🔹 **Function Syntax**
To define a function, we use the `def` keyword, followed by the function name and parameters:
```python
def function_name(parameters):
    # code block
    return result
```

#### Example: Squaring a Number
```python
def square(x):
    return x * x

def main():
    print(square(5))  # Output: 25

main()
```
Here, `square()` takes `x` as an argument and returns `x` multiplied by itself.

#### Return vs Print:
- `return` sends the result back to the caller.
- `print` just displays it on the screen without giving back anything.

Example:
```python
def add(x, y):
    return x + y

def main():
    result = add(3, 4)
    print(result)  # Output: 7

main()
```
The `add()` function returns a value, which is then printed inside `main()`.

---

## 🧠 Part 3: Function Practice

Now let’s get hands-on with a few more examples to solidify the concept.

### 🔹 **Say Hello Function**
```python
def say_hello():
    print("Hello!")

def main():
    say_hello()

main()
```
Here, `say_hello()` doesn't take any parameters but performs a simple task—printing "Hello!".

### 🔹 **Personalized Greeting**
```python
def greet(name):
    print(f"Hi, {name}!")

def main():
    greet("Alice")
    greet("Bob")

main()
```
This example introduces the concept of parameters: we pass the name to `greet()` to customize the message.

### 🔹 **Function with Multiple Parameters**
```python
def add(a, b):
    return a + b

def main():
    result = add(5, 7)
    print(result)  # Output: 12

main()
```
Functions can have as many parameters as needed. In this case, `add()` takes two parameters, `a` and `b`, and returns their sum.

---

## 🔄 Part 4: Function Challenges

Let’s make it a bit more challenging with some real-world function scenarios.

### 🔹 **Challenge 1: Calculator Function**
Create a function that can perform basic arithmetic operations like addition, subtraction, multiplication, and division.

```python
def calculator(x, y, op):
    # Implement the operations (you'll use these in the next lesson)
    pass

def main():
    print(calculator(5, 3, "add"))   # Expected output: 8
    print(calculator(5, 3, "sub"))   # Expected output: 2
    print(calculator(5, 3, "mul"))   # Expected output: 15
    print(calculator(5, 3, "div"))   # Expected output: 1.666...

main()
```

(You'll implement the actual operations in the next lesson when we introduce `if` statements!)

### 🔹 **Challenge 2: Is the Number Even or Odd?**
```python
def is_even(n):
    # You will implement this in the next lesson
    pass

def main():
    print(is_even(4))    # Expected output: True
    print(is_even(5))    # Expected output: False

main()
```

We’ll implement the logic for checking even or odd in the next lesson, but the function definition itself is already set!

---

## ⚡ Part 5: Using the `math` Module

Now that we've learned the basics of functions, let's add some **mathematical power** using the `math` package, which allows you to perform complex mathematical operations with ease.

### 🔹 **Square Root Function**
The `math.sqrt()` function calculates the square root of a number.
```python
import math

def square_root(x):
    return math.sqrt(x)

def main():
    print(square_root(25))  # Expected output: 5.0

main()
```
In this case, `square_root()` takes a number, applies `math.sqrt()`, and returns the result.

### 🔹 **Power Function**
You can also raise a number to a power using `math.pow()`.
```python
def power(base, exponent):
    return math.pow(base, exponent)

def main():
    print(power(2, 3))  # Expected output: 8.0

main()
```
This example shows how to compute `base^exponent` using the `math.pow()` function.

### 🔹 **Trigonometric Functions**
The `math` module also provides trigonometric functions like `math.sin()`, `math.cos()`, and `math.tan()`, but remember they require the angle to be in **radians**, not degrees. Use `math.radians()` to convert degrees to radians.

```python
def sine(angle):
    return math.sin(math.radians(angle))

def main():
    print(sine(90))  # Expected output: 1.0

main()
```

### 🔹 **Logarithms**
You can also work with logarithms using `math.log()`. By default, it calculates the natural logarithm, but you can specify a different base.
```python
def logarithm(x, base):
    return math.log(x, base)

def main():
    print(logarithm(100, 10))  # Expected output: 2.0

main()
```

---

## 🧠 Recap

- **Functions** allow you to bundle code and reuse it with different inputs.
- Use `def` to define a function.
- `return` sends a result back to the caller, while `print` only displays it.
- Functions can have parameters and return values.
- The `math` package provides powerful functions for advanced math operations like square roots, powers, trigonometry, and logarithms.
- Functions help keep your code organized and avoid repetition.

---

## 🚀 What’s Next?

Up next: **Control Flow** — learning how to make decisions in your programs using `if`, `elif`, and `else`. Stay tuned for some exciting challenges ahead!

