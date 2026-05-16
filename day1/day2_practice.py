# ============================================
# 30 Days of Python - Day 02
# Topic: Variables, Data Types & User Input
# ============================================

# --- 1. Variables & Basic Data Types ---

name = "Gemi"               # str  (string)
age = 21                    # int  (integer)
height = 5.7                # float
is_student = True           # bool (boolean)

print("=== My Info ===")
print("Name   :", name)
print("Age    :", age)
print("Height :", height, "ft")
print("Student:", is_student)

# --- 2. type() function ---

print("\n=== Data Types ===")
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>

# --- 3. Type Casting ---

print("\n=== Type Casting ===")
num_str = "42"
num_int = int(num_str)          # str → int
num_float = float(num_str)      # str → float
back_to_str = str(num_int)      # int → str

print("String to int  :", num_int,   type(num_int))
print("String to float:", num_float, type(num_float))
print("Int to string  :", back_to_str, type(back_to_str))

# --- 4. String Operations ---

print("\n=== String Operations ===")
first = "Python"
second = "Zindabad"

# Concatenation
print(first + " " + second)

# f-string (modern & clean way)
print(f"Length of '{first}': {len(first)}")
print(f"Uppercase: {first.upper()}")
print(f"Lowercase: {second.lower()}")
print(f"Replace:   {second.replace('Zindabad', 'Rocks')}")

# --- 5. Multiple Assignment ---

print("\n=== Multiple Assignment ===")
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

a = b = c = 100   # same value to multiple vars
print(f"a={a}, b={b}, c={c}")

# --- 6. User Input (interactive) ---

print("\n=== User Input ===")
user_name  = input("Apna naam likho: ")
user_age   = int(input("Apni umar likho: "))   # input always returns str, so cast

print(f"\nSalam {user_name}! Tum {user_age} saal ke ho.")
print(f"10 saal baad tum {user_age + 10} saal ke hoge. 😄")

# --- 7. Constants (by convention, ALL_CAPS) ---

PI = 3.14159
GRAVITY = 9.8
APP_NAME = "FitTrack"

print("\n=== Constants ===")
print(f"PI       = {PI}")
print(f"Gravity  = {GRAVITY} m/s²")
print(f"App Name = {APP_NAME}")

# --- 8. Practice Challenge ---

print("\n=== Mini Challenge: Simple Bill Calculator ===")
item   = input("Item ka naam: ")
price  = float(input("Price (₹): "))
qty    = int(input("Quantity: "))
total  = price * qty

print(f"\n{qty}x {item} @ ₹{price} = ₹{total:.2f}")
