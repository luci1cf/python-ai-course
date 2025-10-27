# Comprehensions in Python (Create great One-Liners)

# If Statement Comprehensions
# toggle = False
# if toggle:
#     word = 'Enabled'
# else:
#     word = 'Disabled'

# word = 'Enabled' if toggle else 'Disabled'
#
# print(word)

# List Comprehensions With Conditions
# items = ['item_a', 'item_b', 'item_c', 'wrong_data']

# upper_items = []
# for item in items:
#     upper_items.append(item.upper())

# upper_items = [item.upper() for item in items if 'item_' in item]
#
# print(upper_items)

# Exercise With List
# numbers = [1, 2, 3, 4, 5]
# num_sq = [num**2 for num in numbers]
# num_cube = [num**3 for num in numbers]
# num_cube_even = [num**3 for num in numbers if num % 2 == 0]
# even_odd = ['Even' if num % 2 == 0 else 'Odd' for num in numbers]
#
# print(num_sq)
# print(num_cube)
# print(num_cube_even)
# print(even_odd)
#
# mats = ["wood", "steel", "concrete", "bricks", "glass", "plaster"]
# mats = [mat for mat in mats if 's' in mat]
# print(mats)

# Dict Comprehensions
mats = ["wood", "steel", "concrete", "bricks", "glass", "plaster"]
dict_mats = {mat:mat for mat in mats}
print(dict_mats)