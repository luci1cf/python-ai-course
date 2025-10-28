# Collection Data-Types in Python (List | Tuple | Set | Dictionary)
#----------------------------------------------------------
# List  |         | Mutable     | Ordered   | Collection |
# Tuple |         | Immutable   | Ordered   | Collection |
# Set   | Unique  | Mutable     | Unordered | Collection |
# Dict  | Mapped  | Mutable     | Ordered   | Collection |
#----------------------------------------------------------

# Mutable -> you can make changes, immutable -> you CAN'T make changes

# LIST (Mutable Ordered Collection) - Used in 90% Cases!
#-------------------------------------------------------
# Syntax
#-------------------------------
empty_list = [] # or list()
# my_list = ['Wall', 'Floor', 'Roof', 'Ceiling']

# Get Single List Item
#-------------------------------
# print(my_list)
# print(my_list[0])   # First Item (count starts from 0)
# print(my_list[2])   # Third Item (count starts from 0)
# print(my_list[-1])  # Last Item
# print(my_list[-2])  # Second Last Item
# print(my_list[100]) # IndexError: list index out of range

# Get Multiple Items (Slice)
#-------------------------------
# my_list = ['Wall', 'Floor', 'Roof', 'Ceiling','Wall', 'Floor', 'Roof', 'Ceiling']

# print(my_list[:2])      # Get Until 2nd Item (excl.)
# print(my_list[2:])      # Get From 2nd Item (incl.)
# print(my_list[1:3])     # Get From First (incl.) until Third (excl.)
# print(my_list[::2])     # Get Every 2nd Item
# print(my_list[2:6:2])   # Get Every 2nd Item from 2nd (incl.) until 6th (excl.)
# print(my_list[::-1])    # Trick to Reverse List

# Slicing Use-Case Example
# my_list = ['Categories', 'Wall', 'Floor', 'Roof', 'Ceiling']
# header  = my_list[0]
# data    = my_list[1:]
# print(header)
# print(data)

# Membership Operators (Necessary for Logic)
#------------------------------
# my_list = ['Wall', 'Floor', 'Roof', 'Ceiling']
#
# print('Wall' in my_list)
# print('wall' in my_list)
# print('Door' not in my_list)

# Popular Functions with Lists
#--------------------------------
# my_list = ['Wall', 'Floor', 'Roof', 'Ceiling']
# numbers = [10, 20, 30, 40, 50]
# print(len(my_list))         # Get Length
# print(sorted(my_list))      # Create new sorted list
# print(sum(numbers))         # Sum Numbers
# print(min(numbers))         # Get Min Value
# print(max(numbers))         # Get Max Value

# List Methods (Built-In Functionality)
#--------------------------------
# my_list     = ['Wall', 'Floor', 'Roof', 'Ceiling', 'Floor']
# my_list2    = ['Door', 'Window']

# my_list.append('Door')        # Add Single Item
# my_list.extend(my_list2)      # Join 2 Lists
# my_list += my_list2           # Join 2 Lists
# my_list.sort()                # Sort List Alphanumerically
# print(my_list.count('Door'))  # Count value inside list
# print(my_list.index('Wall'))  # Find index of value
# my_list.insert(2, 'Sofa')     # Insert Item at certain Index
# my_list.remove('Floor')       # Remove Value from List (if possible)
# item = my_list.pop(2)         # Remove and Return Value at given Index (last by default)
# my_list.reverse()             # Reverse List Order
# my_list.clear()               # Clear all items from the list
# my_list = []
# y = my_list.copy()            # Create independent copy of a list!

# Nested Lists
#--------------------------------
# points = [
#     [0,0,0],
#     [2,2,0],
#     [4,4,0],
#     [6,6,0]
# ]
#
# pt2 = points[1]
# print(points[1][2])
# print(pt2[0], pt2[1], pt2[2])

# Loops
#--------------------------------
# my_list = ['Wall', 'Floor', 'Roof', 'Ceiling']
#
# for i in my_list:
#     print(i)

# TUPLES (Immutable Ordered Collection)
#------------------------------------------------------------
# empty_tuple = () # or tuple()
# list_data = [0,1,2,3,4,5,0,1,2,3,4,5]       # List Can Be Modified (Mutable)
# data      = (0,1,2,3,4,5,0,1,2,3,4,5)       # Tuples Can't Be Modified (Immutable)
# data_pts  = ((0,0,0), (1,2,3), (2,4,6))     # Nested Tuples Example

# Get Single List Item
#--------------------------------
# print(data[0])
# print(data[2])
# print(data[4])
# print(data_pts[1])

# You Can't Change Tuple Item!
# data[0] = 'New Value'
# print(data)

# Get Multiple Items (Slice)
#-------------------------------
# print(data[:2])      # Get Until 2nd Item (excl.)
# print(data[2:])      # Get From 2nd Item (incl.)
# print(data[1:3])     # Get From First (incl.) until Third (excl.)

# Popular Functions mit Tuples
#-------------------------------
# print(len(data))            # Get length
# print(min(data))            # Min value
# print(max(data))            # Max value
# print(sum(data))            # Sum Numbers
# print(sorted(data))         # Create new sorted list
# print(tuple(sorted(data)))  # Convert List Into Tuple

# Tuple Methods (Built-In Functionality)
#-------------------------------
# data = (0,1,2,3,4,5,0,1,2,3,4,5)
# print(data.count(0))
# print(data.index(3))

# SETS (Unordered Unique Collection)
#--------------------------------------------------------
empty_set = set()
set_items = {10, 20, 30, 10, 20, 'AB', 'BA', 'AB', True, True, False}
# print(set_items)

# Convert List/Tuple
#---------------------------------
# list_data        = [1,2,3,4,1,2,3,4]
# set_data         = set(list_data)
# unique_list_data = list(set_data)
#
# print(list_data)
# print(set_data)
# print(unique_list_data)

# Set Methods (Built-In Functionality)
#---------------------------------
items = {10, 20, 30, 'AB', 'BA', 'AB', True, True, False}

# copy_set = items.copy()     # Copy the set
# removed = items.pop()       # Remove & return a element
# items.clear()               # Remove all elements
# items.remove(3)             # Remove element (error if missing)
# items.discard(3)            # Remove element (no error if missing)
# items.add(10)               # Add a single element

# Set Methods: Compare Sets
#---------------------------------
# a = {1,2,3,4}
# b = {3,4,5,6}
#
# print(a.union(b))                     # Join 2 Sets
# print(a.intersection(b))              # Find I ems in BOTH sets
# print(a.difference(b))                # Set A items that are missing in set B
# print(a.symmetric_difference(b))      # Symmetric difference between 2 sets
# print(a.issubset(b))                  # Is set a completely inside set b?
# print(a.issuperset(b))                # Does set s contain all set b?

# Popular Function with Sets
#---------------------------------
# a = {1,2,3,4}
# print(len(a))       # Count of elements
# print(min(a))       # Minimum
# print(max(a))       # Maximum
# print(sum(a))       # Sum
# print(sorted(a))    # Sorted list

# DICTIONARIES (Mapped Ordered* Mutable Collection)
#---------------------------------------------------------------------
empty_dict = {} # or dict()
dict_example = {'key1' : 'value1', 'key2' : 'value2'}

example_list = ['value1', 'value2']

# Get Items
print(dict_example['key1'])
print(dict_example['key2'])