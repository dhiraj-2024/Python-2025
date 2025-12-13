"""
1. Perform string concatenation
Concatenate 'Thirty', 'Days', 'Of', 'Python' into "Thirty Days Of Python"
Concatenate 'Coding', 'For', 'All' into "Coding For All"
"""

s1 = "Thirty"
s2 = " Days"
s3 = " Of"
s4 = " Python"
full_str = s1 + s2 + s3 + s4
print(full_str)

a = "Coding"
b = " For"
c = " All"

full_str2 = a + b + c
print(full_str2)

# *************************************************************************


"""
2. Check string length
Use len() to get length of a string.
"""
print(len(a))
print(len(s1))
print(len(c))

# *************************************************************************

"""
3. Apply string case methods
Convert a string to:
upper()
lower()
capitalize()
title()
swapcase()
"""
str1 = "hello python"

print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.title())
print(str1.swapcase())

# *************************************************************************

"""
4. Slice and extract portions of a string
Cut out the first word of "Coding For All".
"""

sent = "Coding For All very bad very happy very angry"
cut_first_word = sent[0:6]
v2 = sent[6:]
print(cut_first_word)
print(v2)

"""
# *************************************************************************
5. Search for substrings
Very important for interviews:
Check if a word exists using:
find()
index()
rfind()
rindex()
Examples:
Find position of "Coding" in "Coding For All"
Find the last occurrence of "l" using rfind()
"""
a1 = "Coding For All is very imp For All Student"
print(a1.find("All"))
print(a1.index("Coding"))
print(a1.rfind("l"))
print(a1.rindex("For"))


# *************************************************************************
"""
6. Replace words inside a string
Replace "Coding" with "Python"
Replace text inside "Python for Everyone" → "Python for All"
"""
sample_str = "Python for Everyone"
replace_sample_str = sample_str.replace("Everyone", "All")
print(replace_sample_str)

# *************************************************************************
"""
7. Splitting and joining
Split a string by space
Split a comma-separated list
Create a joined string using join()
"""
Str_11 = "hello How, are you boys"
split_str_spaces = Str_11.split()
print(split_str_spaces)
split_str_comma = Str_11.split(", ")
print(split_str_comma)

splited_str = ('hello', 'How', 'are', 'you', 'boys')

join_str = "# ".join(splited_str)
print(join_str)
# *************************************************************************
"""
8. Indexing
Find:
character at index 0
character at index 10
last index of a string
"""
ex = "this is python series "
print(ex[0])
print(ex[12])
print(len(ex) - 1)


# *************************************************************************
"""
9. Acronyms and abbreviations
Create acronyms from:
"Python For Everyone"
"Coding For All"
"""


# *************************************************************************
"""
10. Check string start/end
startswith("Coding")
endswith("coding")
"""
check_str = "Coding is important or not"
print(check_str.startswith("Coding"))
print(check_str.endswith("Coding"))

# *************************************************************************
"""
11. Strip spaces
Remove left and right spaces using .strip()
"""
strip_str = "   hello dfadfa     sadfasd. "
print(strip_str.strip())
# *************************************************************************
"""
12. Validate identifiers
Which is a valid Python identifier?
"30DaysOfPython"
"thirty_days_of_python" (Valid)
"""
s4 = "30DaysOfPython"
print(s4.isidentifier())
s5 = "thirty_days_of_python"
print(s5.isidentifier())


# *************************************************************************
"""
13. Escape sequences
Use newline \n
Use tab \t
Print strings with formatted alignment
"""

print("asdjfa sdjflaj ckjaklsdjf \n asdkfljadiad alsdkfjao \t hello its tab space default value is 8")

# *************************************************************************
"""
14. String formatting
Use .format() or f-string to print:
Circle area:
radius = 10
area = 3.14 * radius ** 2
"The area of a circle with radius 10 is 314 meters square."
"""
radius = 10
area = 3.14 * radius ** 2
circle_area = "The area of a circle with radius {r} is {a} meters square."
print(circle_area.format(r=radius, a=area))


# *************************************************************************
"""

✔ 15. Mathematical expressions with formatting

Using string formatting to output:

8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""
a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")  # format to 2 decimal places
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")


a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))   # 2 decimal places
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))
