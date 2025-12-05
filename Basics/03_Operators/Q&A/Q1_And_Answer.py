"""
1. Declare your age as integer variable
2. Declare your height as a float variable
3. Declare a variable that store a complex number
4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    # Enter base: 20
    # Enter height: 10
    # The area of the triangle is 100
    
5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
    # Enter side a: 5
    # Enter side b: 4
    # Enter side c: 3
    # The perimeter of the triangle is 12
6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))


"""


# 1,2,3

age = int(23)
height = float(5.8)
complex_num = 3 + 4j


# 4

base =  float(input("enter base :"))
t_height = float(input("enter height :"))

area_of_triangle = 0.5 * base * t_height

print(area_of_triangle)


# 5 calculate peremeter of triangle 

a = float(input("enter side a :"))
b = float(input("enter side b :"))
c = float (input("enter side c :"))

perimeter_of_triangle = a + b + c 

print(perimeter_of_triangle)


# 6 take l and b of rectangle and calculate area and perimeter of rectangle 

l = float(input("enter lenght of recatangle :"))
b = float(input("enter breadth of reactangle :"))

area_of_rectangle = l * b
perimeter_of_rectangle = 2 * ( l * b )

print("area of rectangle is : ", area_of_rectangle)
print("perimeter of rectangle is :",perimeter_of_rectangle)


for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
