# CREATE TUPEL

# syntax
tpl = ('item1', 'item2', 'item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

tupelFirst = ("hello","hii","hey","good")
print(tupelFirst)

# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()


# **************************************************************************************************
# TUPEL LENGTH

print(len(fruits))


# **************************************************************************************************

# ACCESSING TUPEL ITEMS

# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1

print(first_fruit)

print(fruits[2])
print(fruits[3])

# NEGATIVE INDEX 
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_index = len(fruits) - 1
print(first_fruit)


# **************************************************************************************************

# SLICING TUPEL
# We can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple, the return value will be a new tuple with the specified items.

# Range of Positive Indexes

# Syntax
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits = fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]

# Range of Negative Indexes

# Syntax
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]



# **************************************************************************************************

# CHANGING TUPEL INTO LIST

# We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.

# Syntax
tpl = ('item1', 'item2', 'item3', 'item4')
lst = list(tpl)
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')


# **************************************************************************************************

# CHECKING ITEMS IN TUPEL

# We can check if an item exists or not in a tuple using in , it returns a boolean.

# Syntax
tpl = ('item1', 'item2', 'item3', 'item4')
'item2' in tpl  # True
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)  # True
print('apple' in fruits)  # False
fruits[0] = 'apple'  # TypeError: 'tuple' object does not support item assignment

# **************************************************************************************************

# JOINING TUPELS

# We can join two or more tuples using + operator

# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl1 + tpl2
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables


# **************************************************************************************************

# DELETING TUPEL

# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits


