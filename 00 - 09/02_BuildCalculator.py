# Learn about Input and Data Conversion
from stringprep import in_table_a1

str_num_a = input('Enter First Number: ')
str_num_b = input('Enter Second Number: ')

num_a = float(str_num_a)
num_b = float(str_num_b)

total = num_a + num_b
# print(total)

# DataTypes Functions
# str()
# float()
# int()
# bool()
#
# list()
# tuple()
# set()
# dict()

# Convert DataTypes:

# Numbers
x          = 10
str_x      = str(x)     # Convert integer to string: '10'
float_x    = float(x)   # Convert integer to float: 10.0
bool_x     = bool(x)    # Convert integer to boolean: True (non-zero is True)
bool_neg_x = bool(0)    # Convert 0 to boolean: False

# Strings
s          = "123"
int_s      = int(s)     # Convert string to integer: 123
float_s    = float(s)   # Convert string to float: 123.0
bool_s     = bool(s)    # Convert string to boolean: True (if not empty)
bool_empty = bool("")   # Convert empty string to boolean: False

# Booleans
bool_true   = bool(1)           # True
bool_false  = bool(0)           # False
bool_list   = bool([[],[]])     # Convert empty list to boolean: False
bool_dict   = bool({})          # Convert empty dict to boolean: False
bool_str    = bool("Hello")     # Convert non-empty string to boolean: True