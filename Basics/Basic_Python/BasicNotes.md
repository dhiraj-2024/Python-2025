Python Basics - Complete Notes for Interview Revision
=====================================================

This document provides a concise and comprehensive review of fundamental Python concepts, essential for revision and interview preparation.

* * * * *

Table of Contents
-----------------

-   Print Statements

-   Comments

-   Variables

-   Data Types

-   Interview Tips

-   Quick Revision Checklist

* * * * *

1\. Print Statements
--------------------

### Basic Print Function

The `print()` function is used to output text and data to the console.

Python

```
print("hello World")
print("This is the beginning of Python programming!")

```

### Print in Same Line

Use the **`end`** parameter to control the character printed at the end of the output (default is a newline `\n`).

Python

```
print("Hello", end=" ")
print("World!")
# Output: Hello World!

```

### Printing Numbers and Expressions

You can print raw numbers or the result of arithmetic expressions.

Python

```
print(33)           # Integer
print(3.14)         # Float
print(-7)           # Negative number
print(4 + 7)          # Expression evaluation
print("Addition of 4 and 7 is : ", 4 + 7)  # Combined text and expression

```

* * * * *

2\. Comments
------------

Comments are non-executable lines used for code explanation and documentation.

### Single-Line Comments

Use the hash symbol (`#`).

Python

```
# This is a single line comment

```

### Multi-line Comments (Docstrings)

Python uses **triple quotes** (`'''` or `"""`) for blocks of documentation (Docstrings), which function as multi-line comments when not assigned to a variable.

Python

```
'''
This is a
multi-line comment
using triple quotes
'''

"""
This also works
with double quotes
"""

```

* * * * *

3\. Variables
-------------

### Variable Declaration and Assignment

Python is **dynamically typed**, meaning you don't need to declare the type of a variable; it's determined at runtime.

Python

```
# Python is dynamically typed - no need to declare variable types
name = "John"
age = 25
height = 5.9
is_student = True

# Multiple assignment
x, y, z = 10, 20, 30
a = b = c = 100

```

### Variable Naming Conventions

Follow **snake_case** for variable and function names.

Python

```
snake_case = "recommended for Python"
camelCase = "not recommended"
PascalCase = "used for classes"

```

### Variable Types and Memory

You can check a variable's type and memory address using `type()` and `id()`.

Python

```
# Check variable type
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>

# Memory address
print(id(name))      # Memory location of the variable

```

* * * * *

4\. Data Types
--------------

### Basic Data Types

| **Type** | **Examples** | **Description** |
| --- | --- | --- |
| **Numeric** | 10, 10.5, 3 + 4j | `int`, `float`, `complex` |
| **Boolean** | True, False | Represents truth values |
| **String** | "Hello Python", 'A' | Sequence of characters (`str`) |
| **None Type** | None | Represents the absence of a value |

Python

```
# Numeric Types
integer_num = 10
float_num = 10.5
complex_num = 3 + 4j

# Boolean
is_true = True
is_false = False

# String
text = "Hello Python"

# None Type
empty_value = None

```

### Type Conversion

#### Implicit Conversion

Handled automatically by Python (e.g., when an integer and float are operated on).

Python

```
result = 5 + 2.5    # int + float = float (result is 7.5)

```

#### Explicit Conversion (Type Casting)

Manually converting one type to another using functions like `int()`, `str()`, etc.

Python

```
str_to_int = int("10")
int_to_str = str(100)
float_to_int = int(10.7)  # Truncates to 10

```

* * * * *

5\. Interview Tips
------------------

### Common `print()` Function Questions

| **Question** | **Answer** |
| --- | --- |
| What does **`end`** parameter do in `print()`? | Controls what is printed at the end of the output (default is newline `\n`). |
| How to format output in `print()`? | Use **f-strings** (preferred, Python 3.6+), `.format()` method, or the older `%` formatting. |

Python

```
name = "Alice"
age = 30
print(f"{name} is {age} years old")  # f-string (Python 3.6+)
print("{} is {} years old".format(name, age))  # format method

```

### Variable-Related Questions

| **Question** | **Answer** |
| --- | --- |
| Is Python statically or dynamically typed? | **Dynamically typed** -- types are determined at runtime. |
| What is type inference? | Python automatically infers the variable type based on the assigned value. |
| Difference between **`is`** and **`==`**? | **`is`** checks **identity** (same memory location). **`==`** checks **equality** (same value). |

### Memory Management Questions

| **Concept** | **Explanation** |
| --- | --- |
| **Memory Handling** | Python uses automatic garbage collection, primarily a **reference counting mechanism**. |
| **Mutable Types** | Can be changed after creation (e.g., `list`, `dict`, `set`). |
| **Immutable Types** | Cannot be changed after creation (e.g., `int`, `float`, `str`, `tuple`). |

### Common Beginner Mistakes to Avoid

Python

```
# 1. Using undefined variables
# print(undefined_var)  # Leads to NameError

# 2. Incorrect indentation (Indentation is mandatory in Python)
# if True:
# print("hello")  # Leads to IndentationError

# 3. Modifying immutable types
# text = "hello"
# text[0] = "H"  # Leads to TypeError

# 4. Using keywords as variables
# class = "Math"  # Leads to SyntaxError

```

* * * * *

Quick Revision Checklist
------------------------

-   Print statements and formatting (especially `end` and f-strings).

-   Variable declaration and **snake_case** naming.

-   Basic data types (`int`, `float`, `str`, `bool`, `None`) and type conversion.

-   Understanding dynamic typing.

-   Comments and the role of Docstrings.

-   Memory concepts: **Mutable** vs. **Immutable** types.

-   Common errors and debugging.