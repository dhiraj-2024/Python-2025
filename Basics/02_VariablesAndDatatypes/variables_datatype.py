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

print(len(myvar))

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
print("Fruit 1 :", l)
print("Fruit 2 :",m)
print(n)


# GLOBAL VARIABLE

p = "happy"

def myfunc():
    print("dhiraj is " + p)
myfunc()


# first_name = input("enter first name :")
# age = input ("enter your age :")

# print(first_name)
print (age)

# DATA TYPES

f_name = "dhiraj" #str
city = "nashik" #str
age = 23 #int
height = 5.9  #float

print(type(f_name ))
print(type(city ))
print(type(age))
print(type(height))
print(type(3 + 33j)) # complex
print(type(True))  #bool
print(type(False))
print(type(["apple", "banana", "cherry"])) #list
print(type(("apple", "banana", "cherry"))) #tuple
print(type(range(6))) #range
print(type({"name" : "dhiraj", "age" : 22})) #dict
print(type({"apple", "banana", "cherry"}))
print(type(frozenset({"apple", "banana", "cherry"})))
print(type(b"Hello"))