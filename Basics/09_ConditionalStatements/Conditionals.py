# if condition
age = 45
if age > 21:
    print("your are an adult")


# if else condition

if age < 21:
    print("you can not dirive the car")
else:
    print("you can drive the car")


# if elif else conditions

if age < 18:
    print("you can't vote")
elif age <= 18:
    print("you can vote")
else:
    print("you can vote you are above 18 ")


# short hand condition

print("you can marry ") if age > 18 else print("you can not marry ")


# nested condition

a = -3

if a > 0:
    if a % 2 == 0:
        print(a, " is a positive number and even number")
    else:
        print(a, "is a positive number")
elif a == 0:
    print("the number is zero")

else:
    print(a, "is negative number")


# logical operator with conditional statements

b = 4489

if b % 2 == 0 and b > 0:
    print("the number is posivite and even")
elif b > 0 and b % 2 != 0:
    print("the numbrt is positive and odd")
elif b == 0:
    print("the number is zero")
else:
    ("number is negative")