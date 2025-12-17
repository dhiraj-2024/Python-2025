
# ---------------------------------------------
# 1. Creating a Set
# ---------------------------------------------

# Empty set
st = set()
print(st)            # Output: set()

# Set with items
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)        # Output: {'banana', 'orange', 'mango', 'lemon'}

# ---------------------------------------------
# 2. Getting Set Length
# ---------------------------------------------
print(len(fruits))   # Output: 4

# ---------------------------------------------
# 3. Checking an Item
# ---------------------------------------------
print('mango' in fruits)   # Output: True

# ---------------------------------------------
# 4. Adding Items to a Set
# ---------------------------------------------
fruits.add('lime')
print(fruits)        # lime added

# Add multiple items
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)
print(fruits)

# ---------------------------------------------
# 5. Removing Items from a Set
# ---------------------------------------------
fruits.remove('tomato')  # Removes item (must exist)
print(fruits)

# pop() removes a random element
removed_item = fruits.pop()
print("Removed:", removed_item)
print(fruits)

# ---------------------------------------------
# 6. Clearing Items in a Set
# ---------------------------------------------
demo = {'apple', 'banana'}
demo.clear()
print(demo)          # Output: set()

# ---------------------------------------------
# 7. Deleting a Set
# ---------------------------------------------
temp = {'a', 'b'}
del temp
# print(temp)  # This will give error (deleted)

# ---------------------------------------------
# 8. Converting List to Set
# ---------------------------------------------
fruits_list = ['banana', 'orange', 'mango', 'lemon', 'orange']
unique_fruits = set(fruits_list)
print(unique_fruits)   # duplicates removed

# ---------------------------------------------
# 9. Joining Sets
# ---------------------------------------------
# Using union()
fruits = {'banana', 'orange', 'mango'}
vegetables = {'tomato', 'potato', 'carrot'}
print(fruits.union(vegetables))

# Using update()
fruits.update(vegetables)
print(fruits)

# ---------------------------------------------
# 10. Finding Intersection Items
# ---------------------------------------------
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))  # Output: {0,2,4,6,8,10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.intersection(dragon))  # Output: {'o','n'}

# ---------------------------------------------
# 11. Checking Subset and Superset
# ---------------------------------------------
print(even_numbers.issubset(whole_numbers))      # True
print(whole_numbers.issuperset(even_numbers))    # True

# ---------------------------------------------
# 12. Checking Difference
# ---------------------------------------------
print(whole_numbers.difference(even_numbers))  # {1,3,5,7,9}
print(python.difference(dragon))               # {'p','y','t'}

# ---------------------------------------------
# 13. Symmetric Difference
# ---------------------------------------------
print(python.symmetric_difference(dragon))
# Output: characters not in both sets

# ---------------------------------------------
# 14. Disjoint Sets
# ---------------------------------------------
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))  # True
