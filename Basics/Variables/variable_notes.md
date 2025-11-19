✅ **Python Variables --- Short Notes**
====================================

### **1\. What is a Variable?**

-   A variable stores data in memory.

-   You don't need to declare type because Python is **dynamically typed**.

```python

x = 5       # int
y = "Dhiraj" # string

```
* * * * *

✅ **Casting (Type Conversion)**
===============================

-   Convert values into specific types using built-in functions:

```python
name = str("Dhiraj")
age = int(22)

Useful types → `int()`, `float()`, `str()`, `bool()`
```
* * * * *

✅ **Variable Naming Rules**
===========================

✔ Allowed

-   `myvar`

-   `my_var`

-   `_my_var`

-   `myVar`

-   `MYVAR`

-   `myvar2`

❌ Not Allowed

-   `2myvar` (cannot start with number)

-   `my-var` (no hyphens)

-   `my var` (no spaces)

* * * * *

✅ **Naming Styles**
===================

-   **Camel Case:** `myVariableName`

-   **Pascal Case:** `MyVariableName`

-   **Snake Case:** `my_variable_name` ← most used in Python

* * * * *

✅ **Multiple Variable Assignment**
==================================

Assign multiple values in one line:
```python

a, b, c = "Orange", "Banana", "Cherry"

```
All variables get different values.

* * * * *

✅ **Unpacking a Collection**
============================

Assign list/tuple items into variables:
```python

fruits = ["Banana", "Pineapple", "Mango"]
a, b, c = fruits
```
* * * * *

✅ **Global Variables**
======================

-   Variables created outside functions are **global**.

-   Can be used inside functions unless redefined.

`p = "happy"

def myfunc():
    print("dhiraj is " + p)`

Use `global` keyword to modify inside function:

`def myfunc():
    global p
    p = "sad"`

* * * * *

🧠 **Super Quick Interview Points**
===================================

-   Python variables don't need type declaration.

-   Variable type is decided at runtime.

-   Use `type()` to check type.

-   Use snake_case for professional Python code.

-   Global variables are accessible inside functions unless overshadowed.