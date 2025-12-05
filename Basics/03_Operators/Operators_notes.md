## 1. What is an Operator?
--------------------------

Operators are special symbols used to perform operations on variables and values.

Example:

```
a = 10
b = 5
print(a + b)
```

* * * * *

## ⭐ Types of Operators in Python


1.  Arithmetic Operators

2.  Assignment Operators

3.  Comparison (Relational) Operators

4.  Logical Operators

5.  Identity Operators

6.  Membership Operators

7.  Bitwise Operators

* * * * *

* * * * *

## 2. Arithmetic Operators
--------------------------

Used for mathematical operations.

| Operator | Meaning | Example |
| --- | --- | --- |
| `+` | Addition | `10 + 5 = 15` |
| `-` | Subtraction | `10 - 5 = 5` |
| `*` | Multiplication | `10 * 5 = 50` |
| `/` | Division | `10 / 5 = 2.0` |
| `%` | Modulus (remainder) | `10 % 3 = 1` |
| `**` | Exponent (power) | `2 ** 3 = 8` |
| `//` | Floor division | `10 // 3 = 3` |

### Example:

```
x = 10
y = 3
print(x % y)   # 1
print(2 ** 3)  # 8
print(x // y)  # 3
```

* * * * *

## 3. Assignment Operators
--------------------------

Used to assign values to variables.

| Operator | Example | Meaning |
| --- | --- | --- |
| `=` | `a = 5` | Assign |
| `+=` | `a += 3` | a = a + 3 |
| `-=` | `a -= 3` | a = a - 3 |
| `*=` | `a *= 3` | a = a * 3 |
| `/=` | `a /= 3` | a = a / 3 |
| `%=` | `a %= 3` | a = a % 3 |
| `**=` | `a **= 2` | a = a ** 2 |
| `//=` | `a //= 2` | a = a // 2 |

### Example:

```
a = 10
a += 5
print(a)   # 15
```

* * * * *

## 4. Comparison (Relational) Operators
---------------------------------------

Used to compare two values.

| Operator | Meaning |
| --- | --- |
| `==` | Equal to |
| `!=` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

### Example:

```
x = 10
y = 20
print(x < y)   # True
print(x == y)  # False
```

* * * * *

## 5. Logical Operators
-----------------------

Used to combine conditional statements.

| Operator | Meaning |
| --- | --- |
| `and` | True if both are True |
| `or` | True if any one is True |
| `not` | Reverses True/False |

### Example:

```
x = 5
print(x > 3 and x < 10)  # True
print(x > 10 or x == 5)  # True
print(not(x == 5))       # False
```

* * * * *

##  6. Identity Operators
------------------------

Used to compare object memory location.

| Operator | Meaning |
| --- | --- |
| `is` | True if both refer to same object |
| `is not` | True if not same object |

### Example:

```
a = ["apple", "banana"]
b = a
print(a is b)      # True
print(a is not b)  # False
```

* * * * *

## 7. Membership Operators
--------------------------

Used to check presence of an item in a sequence.

| Operator | Meaning |
| --- | --- |
| `in` | True if present |
| `not in` | True if not present |

### Example:

```
fruits = ["apple", "banana", "mango"]
print("apple" in fruits)      # True
print("orange" not in fruits) # True
```

* * * * *

## 8. Bitwise Operators (Important for interviews)
--------------------------------------------------

Works on binary numbers (0s and 1s).

| Operator | Meaning |
| --- | --- |
| `&` | AND |
| ` | ` |
| `^` | XOR |
| `~` | NOT |
| `<<` | Left shift |
| `>>` | Right shift |

### Example:

```
x = 6   # 110
y = 3   # 011

print(x & y)  # 2  (010)
print(x | y)  # 7  (111)
print(x ^ y)  # 5  (101)
```

* * * * *

🟢 Interview Quick Points
=========================

✔ `==` checks **value**, but `is` checks **identity/memory**\
✔ `and`, `or`, `not` are called **logical operators**\
✔ `%` is used to find remainder\
✔ `//` removes decimal part (floor division)\
✔ `**` used for power

* * * * *

🟢 Mini Practice Questions
==========================

1.  What is the difference between `==` and `is`?

2.  What is floor division? Give an example.

3.  What is the output of `2 ** 3`?

4.  How does `in` operator work?

5.  What is the difference between `a += 5` and `a = a + 5`?