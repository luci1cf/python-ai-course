# Recursive Function (Function that can call itself)

# Iterative Countdown
#------------------------------------------------------------------------------
# def countdown(n):
#     while True:
#         if n < 0:
#             break
#         print(n)
#         n -= 1
#
# print('Iterative: ')
# countdown(5)
# print('-'*50)

# Recursive Countdown
#-----------------------------------------------------------------------------
# def countdown2(n):
#     # Base Case
#     if n < 0:
#         return
#
#     # Recursive Case
#     print(n)
#     countdown2(n-1)
#
# print('Recursive: ')
# countdown2(5)
# print('-'*50)


# What's factorial?
# - The product of all numbers from 1 to n.
# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120

# Factorial - Recursive
#-----------------------------------------------------------------
def factorial(n):
    print(f'Entering factorial: {n}')

    if n == 0:      # Base Case
        print('Base Case reached: Returning 1')
        return 1

    result =  n * factorial(n-1)     # Recursive Case
    print(f'Returning {result} for factorialn({n})')
    return result

print('Recursive: ')
print(factorial(5))
print('-'*50)