# Logic - Syntax Basics
# condition = 5 > 0   # True
#
# if condition:
#     print('Code A')
#     print('Code A')
#     print('Code A')
#
# print('Code B')
from faulthandler import is_enabled

# Example If/Elif/Else
# temp = -50
#
# if temp > 25:
#     print("It's really hot outside")
#
# elif temp > 15:
#     print("It's warm outside")
#
# elif temp > 0:
#     print("It's chill outside")
#
# else:
#     print("It's freezing cold")

# Comparison Operators
equal               = 5 == 5  # True
not_equal           = 3 != 3  # False
greater_than        = 7 > 5   # True
less_than           = 7 < 5   # False
greater_than_eq     = 5 >= 5  # True
less_than_eq        = 5 >= 6  # False

# Logical Operators
logical_and = True and True # True
logical_or = True or True   # True
logical_not = not True      # False

# X = 20
# Y = 40
#
# if X > 0 and X < 100 and Y > 0 and Y < 100:
#     print('XY Coordinate is good.')

# if X > 0:
#     if X < 100:
#         if Y > 0:
#             if Y < 100:
#                 print('XY Coordinate is good.')

# if Y > 0 and Y < 100:
#     print('Y Coordinate is good.')

# Membership Operators
# member_in       = 'wood'        in ['metal', 'concrete', 'wood']     # True
# member_in2      = 'w'           in 'wood'                            # True
# member_not_in   = 'wood' not    in ['metal', 'concrete', 'bricks']   # True

# Nested Statements
panel_W = 2000
panel_H = 2500

if panel_W <= 1500:
    print('Width is good.')

    if panel_H <= 3000:
        print('Height is good.')
    else:
        print('Height is not good.')

else:
    print('Width is not good.')
