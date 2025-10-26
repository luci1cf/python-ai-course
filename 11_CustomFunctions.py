# Functions in Python

# Syntax Basics
# def say_hello():
#     print('Hello BIM World!')
#
# say_hello()
# say_hello()
# say_hello()

# Function with Arguments/Parameters
# def greet(name, salutation=''):
#     print('Hello {}{}!'.format(salutation, name))
#
# greet("Erik", 'Mr.')
# greet("Kristina", 'Mrs.')
# greet("Klaus", 'Cato.')
# greet("Ricky", 'Cato.')

# Return Value

def add_numbers(a, b):
    total = a + b
    print('{} + {} = {}'.format(a, b, total))
    return total

x = add_numbers(5, 5)
y = add_numbers(10, 20)
z = add_numbers(25, 25)
print(x, y, z)
