# Basic Operators in Python

# Expression
# x = 10
# y = 20
# z = x + y
#
# print(x,y,z)
# print(x+y+z)

#------------------------------------------------------------------------------
# String Operator

# Join Strings
# a = 'Hello '
# b = 'World'
# c = a + b
# print(c)
# print(a+b)

# name = 'Erik'
# print('My name is: ' + name)
# print('My name is: {}'.format('Erik'))

# Multiply Strings
# print('Hello')
# print('-'*100)
# print('Hello\n'*100)

# Membership Operator in/not in
# message = 'We need to build a brick wall'
# print('brick' in message)       # True
# print('Brick' in message)       # False
# print('glass' in message)       # False
# print('glass' not in message)   # True

# Equal/Not Equal operators (==, !=)
# a = 'Concrete-10cm'
# b = 'Concrete-20cm'
#
# check = a==b
# print(check)     # False
# print(a!=b)      # True

#-------------------------------------------------------------------------------------------------
# Numeric Operators
# a = 10
# b = 3

# Arithmetic Operators
# print("a + b =", a + b)     # 10 + 3 = 13       (Addition)
# print("a - b =", a - b)     # 10 - 3 = 7        (Subtraction)
# print("a * b =", a * b)     # 10 * 3 = 30       (Multiplication)
# print("a / b =", a / b)     # 10 / 3 = 3.33...  (Division)
# print("a // b =", a // b)   # 10 // 3 = 3       (Floor Division)
# print("a % b =", a % b)     # 10 % 3 = 1        (Modulo)
# print("a ** b =", a ** b)   # 10 ** 3 = 1000    (Numeric Power)

# Comparison Operators
# print("a > b =", a > b)     # 10 > 3 = True       (Greater Than)
# print("a < b =", a < b)     # 10 < 3 = False      (Less Than)
# print("a >= b =", a >= b)   # 10 >= 3 = True      (Greater Than or Equal To)
# print("a <= b =", a <= b)   # 10 <= 3 = False     (Less Than or Equal To)
# print("a == b =", a == b)   # 10 == 3 = False     (Equality)
# print("a != b =", a != b)   # 10 != 3 = True      (Inequality)

#------------------------------------------------------------------------------------------------
# List Operators
# mats_1 = ["Concrete", "Steel", "Glass"]
# mats_2 = ["Wood", "Brick"]
# mats_3 = mats_1 + mats_2
# mats_4 = [
#     ["Concrete", "Steel", "Glass"],
#     ["Wood", "Brick"]
# ]
# print(mats_3)

# Multiply Lists
# print(mats_1*10)

# Membership Operators
# print('Concrete' in mats_3)     # True
# print('Wool'     in mats_3)     # False
# print('Wool' not in mats_3)     # True

# print(mats_2 in mats_3)         # False
# print(mats_2 in mats_4)         # True

# Equality
# print(mats_1 == mats_2)     # False
# print(mats_1 != mats_2)     # True
