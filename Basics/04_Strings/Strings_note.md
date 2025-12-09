🟩 1. What is a String?
-----------------------

A **string** is a sequence of characters enclosed in single quotes `' '` or double quotes `" "`.

```
letter = 'P'
greeting = "Hello, World!"
```

✔ Python treats both `' '` and `" "` the same.

* * * * *

🟩 2. String Length
-------------------

Use `len()` to find number of characters.

`len("Hello")`

* * * * *

🟩 3. Multiline Strings
-----------------------

Use triple quotes (`'''` or `"""`) to create multi-line strings.

```
text = """This is
a multiline
string."""
```

* * * * *

🟩 4. String Concatenation
--------------------------

Joining strings using `+` operator.

```
first = "Dhiraj"
last = "Barwal"
full = first + " " + last
```

* * * * *

🟩 5. Unpacking Characters
--------------------------

Assign each character to a variable:

```
language = "Python"
a,b,c,d,e,f = language
```

* * * * *

🟩 6. Indexing (Access Characters)
----------------------------------

📌 Index starts at **0**

```
language = "Python"
print(language[0])   # P
print(language[1])   # y
```

✔ Negative index:

```
print(language[-1])  # n
print(language[-2])  # o
```

* * * * *

🟩 7. String Slicing
--------------------

Get substring using `[start:end]`.

```
language = "Python"
print(language[0:3])   # Pyt
print(language[3:])    # hon
print(language[-3:])   # hon
```

✔ Skipping characters:

`print(language[0:6:2])  # Pto`

* * * * *

🟩 8. Escape Sequences
----------------------

| Escape | Meaning |
| --- | --- |
| `\n` | New line |
| `\t` | Tab space |
| `\\` | Backslash |
| `\"` | Double quote |

```
print("Hello\nWorld")
print("A\tB\tC")
print("He said \"Hi\"")
```

* * * * *

🟩 9. String Formatting
-----------------------

### 🔹 Using `format()`

```
name = "Dhiraj"
city = "Nashik"
print("My name is {} and I live in {}.".format(name, city))
```

* * * * *

🟩 10. Common String Methods
----------------------------

Below are important functions to remember for interviews:

* * * * *

### 🔹 `capitalize()`

Makes first letter uppercase.

`"python code".capitalize()`

* * * * *

### 🔹 `count()`

Count number of occurrences.

`"text text".count("t")`

* * * * *

### 🔹 `endswith()`

Returns True/False.

`"python".endswith("on")`

* * * * *

### 🔹 `expandtabs()`

Replace tab characters with spaces.

* * * * *

### 🔹 `find()`

Returns index of first occurrence, else `-1`.

`"python".find("y")`

* * * * *

### 🔹 `isalpha()`

True if all characters are alphabets.

`"Hello".isalpha()`

* * * * *

### 🔹 `isdigit()`

True if all characters are digits.

`"123".isdigit()`

* * * * *

### 🔹 `isalnum()`

True if only letters + numbers.

`"abc123".isalnum()`

* * * * *

### 🔹 `isidentifier()`

Valid Python variable name?

`"my_variable".isidentifier()`

* * * * *

### 🔹 `islower()` & `isupper()`

Check case.

* * * * *

### 🔹 `isnumeric()` / `isdecimal()`

Numbers only.

* * * * *

### 🔹 `join()`

Convert list → string.

```
"-".join(["A","B","C"])
# A-B-C
```

* * * * *

### 🔹 `strip()`

Remove leading/trailing characters (default: spaces)

* * * * *

### 🔹 `replace()`

Replace substring.

`"python".replace("py", "java")`

* * * * *

### 🔹 `split()`

Turn string into list of words.

`"Hello world".split()`

* * * * *

### 🔹 `title()`

Make each word start with uppercase.

* * * * *

### 🔹 `swapcase()`

Change upper ↔ lower.

* * * * *

### 🔹 `startswith()`

Check beginning of string.

* * * * *

* * * * *

🟢 Important Interview Concepts (Strings)
=========================================

✔ **Strings are immutable**\
Once created, cannot be changed.

✔ **Indexing starts from 0**

✔ **Negative indexing starts from -1**

✔ `split()` returns a list\
✔ `join()` converts list to string

* * * * *

* * * * *

🟢 Quick Interview Questions
============================

1.  What is string immutability?

2.  Difference between `find()` and `index()`?

3.  How do you reverse a string in Python?

4.  How to count occurrences of a substring?

5.  How to check if a string is a valid identifier?

6.  How to remove spaces from start and end of a string?

* * * * *

* * * * *

🟢 Practice Task
================

Try writing code for:

✔ Get the last 3 characters of a string\
✔ Convert a user input string to title case\
✔ Replace all spaces with "-"\
✔ Count vowels in a string