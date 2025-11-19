# CREATE A VARIABLE

x = 5 # integer variable
y = "dhiraj" # string variable

print(y)


# CASTING

name = str("Dhiraj")
age = int(22)

print(type(name))

# VARIABLE NAMES RULES


# allow
myvar = "dhiraj"
my_var = "dhiraj"
_my_var = "dhiraj"
myVar = "dhiraj"
MYVAR = "dhiraj"
myvar2 = "dhiraj"


#not allow

# 2myvar = "dhiraj"
# my-var = "dhiraj"
# my var = "dhiraj"


# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "John"


# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "John"


# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John"


# MULTI VARIABLE ASSIGNMENT

a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)



# UNPACKING A COLLECTION 

fruit =["Banana", "Pineapple", "Mango"]
l , m ,n = fruit
print(m)
print(m)
print(n)


# GLOBAL VARIABLE

p = "happy"

def myfunc():
    print("dhiraj is " + p)
myfunc()