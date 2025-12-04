 ## 1. What is a Variable?
-------------------------

A variable is a container for storing data values.

### Example:

```
x = 5
y = "dhiraj"
```

-   `x` → integer variable

-   `y` → string variable

### Key Point:

-   Python automatically detects the type based on the assigned value.

* * * * *

## 2. Variable Casting
----------------------

Casting means converting one data type into another.

```
name = str("Dhiraj")
age = int(22)
```

-   `str()` → converts to string

-   `int()` → converts to integer

-   `float()` → converts to float

✔️ Use `type()` to check variable type.

`print(type(name))`

* * * * *

## 3. Variable Naming Rules
---------------------------

### ✔ Allowed:

```
myvar
my_var
_my_var
myVar
MYVAR
myvar2
```

### ❌ Not Allowed:

```2myvar   # cannot start with a number
my-var   # hyphen not allowed
my var   # space not allowed
```

* * * * *

## 4. Naming Conventions (Important for Interviews)
---------------------------------------------------

1.  **camelCase** → `myVariableName`

2.  **PascalCase** → `MyVariableName`

3.  **snake_case** → `my_variable_name` (🔥 Most used in Python)

* * * * *

## 5. Multiple Variable Assignment
----------------------------------

Assign multiple values in one line:

`a, b, c = "Orange", "Banana", "Cherry"`

* * * * *

## 6. Unpacking a Collection
----------------------------

If a collection contains 3 items, we can assign them to 3 variables:

```
fruit = ["Banana", "Pineapple", "Mango"]
l, m, n = fruit
```

* * * * *

## 7. Global and Local Variables
--------------------------------

### Global Variable:

Declared outside a function and used anywhere.

```
p = "happy"

def myfunc():
    print("Dhiraj is " + p)
```

### Local Variable:

Declared inside a function, cannot be used outside.

* * * * *

## 8. Input Function (User Input)
---------------------------------

```
# first_name = input("Enter first name: ")
#### age = input("Enter your age: ")
```

-   Everything from `input()` is treated as **string** by default.

* * * * *

## 9. Python Data Types


Python has several built-in data types.

### 🔥 Basic Types

| Type | Example |
| --- | --- |
| `str` | "dhiraj" |
| `int` | 23 |
| `float` | 5.9 |
| `complex` | `3 + 33j` |
| `bool` | True / False |

* * * * *

### 🔥 Collection Types

| Type | Example |
| --- | --- |
| `list` | `["apple", "banana", "cherry"]` |
| `tuple` | `("apple", "banana", "cherry")` |
| `range` | `range(6)` |

* * * * *

### 🔥 Mapping Type

| Type | Example |
| --- | --- |
| `dict` | `{"name": "dhiraj", "age": 22}` |

* * * * *

### 🔥 Set Types

| Type | Example |
| --- | --- |
| `set` | `{"apple", "banana", "cherry"}` |
| `frozenset` | `frozenset({"apple", "banana"})` |

* * * * *

### 🔥 Binary Type

| Type | Example |
| --- | --- |
| `bytes` | `b"Hello"` |

* * * * *

## 10. Checking Data Type
-------------------------

Use `type()` function:

```
print(type(23))           # int
print(type("hello"))      # str
print(type(5.6))          # float
print(type(["a","b"]))    # list
print(type(3+5j))         # complex
print(type(True))         # bool
```

* * * * *

## Interview Quick Points to Remember
=====================================

✔ Variables don't need explicit type declaration in Python (dynamic typing).\
✔ Naming should be meaningful and follow snake_case in Python.\
✔ Use multiple assignment and unpacking for cleaner code.\
✔ Input function always returns string → convert using `int()`, `float()`, etc.\
✔ `type()` is used to verify data type.\
✔ Python has immutable types (str, tuple, frozenset) and mutable types (list, dict, set).

* * * * *

## Bonus Practice Questions


1.  What is dynamic typing?

2.  What is the difference between list and tuple?

3.  What is mutable vs immutable data type?

4.  What is the output of `type(3+4j)`?

5.  Can we assign multiple variables in one line? Give example.

6.  What is a global variable?