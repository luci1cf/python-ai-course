
# Text Variables
#---------------------------------------------------
text   = 'Text in python is called String'
text_2 = "It has to be inside single or double quotes"
text_3 = 'We can use "double-quotes" inside single quotes'
text_4 = "And 'vice-versa' " # This is a string

sum_ = 2+2
# But we can not write text in python without quotes.
# It will break syntax rules...

# Print Statements
#---------------------------------------------------
# print(text)
# print(text_2)
# print(text_3)
# print(text_3)

# Basic Data-Types in Python
#---------------------------------------------------

string     = 'text'
str_number = '10'
num_int    = 10
num_float  = 3.14
boolean    = True # False#
none_type  = None

# print(type(string))
# print(type(str_number))
# print(type(num_int))
# print(type(num_float))
# print(type(boolean))
# print(type(none_type))

# Simple Exercise
#---------------------------------------------------
user = 'Klaus'
app = 'Photoshop'

print(f'Once upon a time, there was a {app} User named {user}')
print(f'{user} wasted months on soul-draining tasks in {app}')
print(f'Until one day {user} said: Enough!')
print(f'And by accident he discovered that he can automate his {app} work with Python')
print(f'But {user} knew nothing about Python.')
print(f'And so, {user} has begun his programming journey.')

# After Python 3.6.6 - f-string or .format()
print(f'My name is {user}')

# Before Python 3.6.6 - .format()
print('My name is: {}'.format(user))

