# 📅 Day 02 — Variables, Data Types & User Input

> **30 Days of Python Challenge**
> `#30DaysOfPython` | Beginner → Intermediate

---

## 🧠 Topics Covered

| # | Topic |
|---|-------|
| 1 | Variables & Basic Data Types (`str`, `int`, `float`, `bool`) |
| 2 | `type()` function |
| 3 | Type Casting (`int()`, `float()`, `str()`) |
| 4 | String Operations (concatenation, f-strings, methods) |
| 5 | Multiple Assignment |
| 6 | User Input with `input()` |
| 7 | Constants (naming convention) |
| 8 | Mini Challenge: Simple Bill Calculator |

---

## 📂 File

```
day02_variables_datatypes.py
```

---

## 💡 Key Concepts

### Variables
```python
name     = "Ali"      # str
age      = 21         # int
height   = 5.7        # float
active   = True       # bool
```

### Type Casting
```python
num = int("42")       # "42" → 42
pi  = float("3.14")   # "3.14" → 3.14
s   = str(100)        # 100 → "100"
```

### f-strings (Recommended way to format output)
```python
name = "Gemi"
print(f"Hello, {name}!")   # Hello, Gemi!
```

### User Input
```python
name = input("Enter your name: ")    # always returns str
age  = int(input("Enter age: "))     # cast to int manually
```

---

## ▶️ How to Run

```bash
python day02_variables_datatypes.py
```

> Make sure Python 3.x is installed. The script will ask for a few inputs interactively.

---

## ✅ Output Preview

```
=== My Info ===
Name   : Gemi
Age    : 21
Height : 5.7 ft
Student: True

=== Data Types ===
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>

=== String Operations ===
Python Zindabad
Length of 'Python': 6
Uppercase: PYTHON
...
```

---

## 🔗 Series Navigation

| Day | Topic | Link |
|-----|-------|------|
| 01  | Hello World, Print, Comments | [Day 01](../Day01/) |
| 02  | Variables, Data Types & Input | ← You are here |
| 03  | Operators & Expressions | Coming soon |

---

*Practicing daily to build real Python skills 💪🐍*
