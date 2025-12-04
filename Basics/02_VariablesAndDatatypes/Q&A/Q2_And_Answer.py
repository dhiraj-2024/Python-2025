"""
1. Check the data type of all your variables using type() built-in function
2. Using the len() built-in function, find the length of your first name
3. Compare the length of your first name and your last name
4. Declare 5 as num_one and 4 as num_two
5. Add num_one and num_two and assign the value to a variable total
6. Subtract num_two from num_one and assign the value to a variable diff
7. Multiply num_two and num_one and assign the value to a variable product
8. Divide num_one by num_two and assign the value to a variable division
9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
10. Calculate num_one to the power of num_two and assign the value to a variable exp
11. Find floor division of num_one by num_two and assign the value to a variable floor_division
12. The radius of a circle is 30 meters.
13. Calculate the area of a circle and assign the value to a variable name of area_of_circle
14. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
15. Take radius as user input and calculate the area.
16. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
17. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
    
"""

# variables 
first_name = "dhiraj"
last_name = "rajput"
full_name = "dhiraj rajput"
country = "India"
city = "nashik"
age = 23
year = 2025
is_married = False
is_true = True
is_light_on = True

# 1. print the data types of all variables 

print ("Type of First_name : ",type(first_name))
print ("Type of Last_name : ",type(last_name))
print ("Type of Full name : ",type(full_name))
print ("Type of India : ",type(country))
print ("Type of Age : ",type(age))
print ("Type of year : ",type(year))
print ("Type of is_married : ",type(is_married))


# 2. find the lenth of first_name using len() function 

print("lenght of first name is : " , len(first_name))

# 3. compare the length of your first_name and last_name

print ("length of first name is : " , len(first_name), "length of last_name is : ", len(last_name))

print (len(first_name) == len(last_name))

# 4. declare num_one and num_two

num_one = 5 
num_two = 4

# 5. add num_one and num_two and assign the value to total
total = num_one + num_two
print ("total is : ", total)

# 6. subtract num_two from num_one and assign the value to diff
sub = num_one - num_two
print ("subtraction is : ", sub)

# 7. multiply num_two and num_one and assign the value to product
multiplication = num_one * num_two
print ("multiplication is : ", multiplication)

# 8. divide num_one by num_two and assign the value to division
division = num_one / num_two
print ("division is : ", division)

# 9. use modulus division to find num_two divided by num_one and assign the value to remainder
reminder = num_two % num_one
print ("reminder is : ", reminder)

# 10. calculate num_one to the power of num_two and assign the value to exp
exponential = num_one ** num_two
print ("exponential is : ", exponential)

# 11. find floor division of num_one by num_two and assign the value to floor_division
floorDivision = num_one // num_two
print ("floorDivision is : ", floorDivision)

# 12. radius of circle is 30 meters
radius = 30

# 13. calculate the area of a circle and assign the value to area_of_circle
area_of_circle = 3.14 * radius * radius
print ("area_of_circle is : ", area_of_circle)

# 14. calculate the circumference of a circle and assign the value to circum_of_circle
circum_of_circle = 2 * 3.14 * radius
print ("circum_of_circle is : ", circum_of_circle)

# 15. take radius as user input and calculate the area.

user_radius = float(input("enter the radius of circle :"))
area_of_circle_user = 3.14 * user_radius * user_radius
print ("area_of_circle_user is : ", area_of_circle_user)


# 16. use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
user_first_name = input("enter your first name : ")
user_last_name = input("enter your last name : ")
user_country = input("enter your country : ")
user_age = input("enter your age : ")
print ("user_first_name : ", user_first_name)
print ("user_last_name : ", user_last_name)
print ("user_country : ", user_country)
print ("user_age : ", user_age)

# 17. run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
