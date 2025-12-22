# create list
myFirstList = ["oneplus", "apple", "samsung", "redmi"]
print(myFirstList)
for x in myFirstList:
    print("item :", x)

# create list using list() constructor
mySecondList = list(("apple", "banana", "cherry"))
print(mySecondList)

# allow duplicate items in list

allow_dup = ["oneplus", "apple", "samsung", "redmi", "apple"]
print(allow_dup)

# print the lenght of list

print(len(allow_dup))
print(len(myFirstList))


# print the type of list : it contain any type of data

# Lists can have items of different data types
lst = ['dhiraj', 22, True, {'country': 'India', 'city': 'Nashik'}]

print(type(allow_dup))  # <class 'list'>
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# **************************************************************************************************

# ACCESS THE LIST ITEMS :

l1 = [22, 55, 33, 4, 322, 555, 324, 87, 445, 7765, 980]
print(l1[8])  # 445
print(l1[1])  # 55

l2 = ["apple", "banana", "cherry"]
print(l2[-1])  # cherry last item
print(l2[-2])  # banana second last like this -3,-4,-5.......

# **************************************************************************************************

# SLICING

# Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. (default values for start=0, end=len(lst) - 1 (last item), step=1)

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]  # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:]  # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3]  # it does not include the first index
orange_mango_lemon = fruits[1:]
# here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
orange_and_lemon = fruits[::2]


# Negative Indexing: We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]  # it returns all the fruits
# it does not include the last index,['orange', 'mango']
orange_and_mango = fruits[-3:-1]
# this will give starting from -3 to the end,['orange', 'mango', 'lemon']
orange_mango_lemon = fruits[-3:]
# a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
reverse_fruits = fruits[::-1]

print(l1[1:5])  # [55, 33, 4, 322]
# >>>>>> First index contain but sencond is not contain in range like 1 consider but 5 not its upto 4
print(l1[1:])
print(l1[5:])
print(l1[-7:-3])


if "banana" in l2:
    print("this is banana")

# **************************************************************************************************

# UNPACKING LIST ITEMS

lst = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)


item1, item2, item3, item4, item5, * \
    other = [1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 6, 5,
             4, 4, 5, 5453, 345, 345, 65, 65, 324, 45]
print(item1)
print(item2)
print(item3)
print(other)

# **************************************************************************************************

# MODIFYING LIST

listm = ["audi", "bmw", "mahindra", "tata", "kia", "toyota", "mercedies"]
print(listm)
listm[1] = "ford"
print(listm)

# **************************************************************************************************

# CHECKING ITEM IN A LIST

listm = ["audi", "bmw", "mahindra", "tata", "kia", "toyota", "mercedies"]
does_exist = "audi" in listm
print(does_exist)  # True

does_exist = "nano" in listm
print(does_exist)

# **************************************************************************************************

# ADD ITEMS IN THE LIST

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)  # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')
print(fruits)  # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']


# **************************************************************************************************

# INSERT ITEMS IN LIST

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
fruits.insert(0, "papaya")
print(fruits)
fruits.insert(4, "grapes")
print(fruits)

# **************************************************************************************************

# REMOVE ITEM FROM LIST
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)
thislist.remove("banana")
print("removed banana from the list : ", thislist)
# **************************************************************************************************

# POP ITEM FROM LIST
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)
thislist.pop(0)
print("pop apple from the list : ", thislist)
thislist.pop()
print("pop last item from list if index in not provided : ", thislist)

# **************************************************************************************************

# DELETE ITEM FROM LIST OR DELETE ENTIRE LIST
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)
del thislist[2]
print("delete cherry from the list : ", thislist)
del thislist[0:2]
print(thislist)
del thislist

# print(thislist)
# **************************************************************************************************

# COPY LIST
orignal = ["apple", "banana", "cherry", "banana", "kiwi"]
copy_list = orignal.copy()
print(copy_list)
# **************************************************************************************************

# JOIN LIST
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
# ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
print(fruits_and_vegetables)

# **************************************************************************************************

# COUNT ITEMS IN LIST

num = [ 1,2,3,4,4,2,2,5,6,7,4,6,7]
print(num.count(4)) # 3
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange')) # 1

# **************************************************************************************************

# FIND THE INDEX OF ITEM

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('mango')) #2


# **************************************************************************************************

# REVERSE THE LIST

fruitss = ['banana', 'orange', 'mango', 'lemon']
fruitss.reverse()
print(fruitss)

# **************************************************************************************************

# SORTING LIST ITEMS

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
# sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
print(fruits)
fruits.sort(reverse=True)
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)  # [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages)  # [26, 25, 25, 24, 24, 24, 22, 19]


# sorted(): returns the ordered list without modifying the original list Example:

fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits, reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
