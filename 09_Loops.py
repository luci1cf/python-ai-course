# Basic Syntax: For Loops
#-----------------------------------------------------
# container =  [1, 2, 3, 4, 5]
#
# for num in container:
#     print(num)
#     print(num)
#     print(num)
#
#     if num == 2:
#         print('Number Two.')

# Loop Over List
#-----------------------------------------------------
# list_materials = ['Wood', 'Steel', 'Glass', 'Bricks']
#
# for mat in list_materials:
#     print(mat)
#     print(mat.lower(), mat.upper())

# Loop Over String
#------------------------------------------------------
# text = 'Hello Python Hackers'
#
# for char in text:
#     lower_char = char.lower()
#     upper_char = char.upper()
#     print(lower_char, '---', upper_char)

# Loop Over Digits
#------------------------------------------------------
# big_number = 123456789
#
# for str_num in str(big_number):
#     num = int(str_num)
#     sq = num**2
#     cube = num**3
#     print(num, sq, cube)

# Iterate Over Range
#-------------------------------------------------------
# for i in range(50):
#     print('Hello World')

# floor_plans = []
#
# for i in range(1, 11):
#     plan_name = f'FloorPlan_{i}'
#     floor_plans.append(plan_name)
#
# print(floor_plans)

# Break Out of For-Loops
#-------------------------------------------------------
# nums = [0, 99, 1, 23, 33, 40, 57, 6, 81]
#
# for n in nums:
#     if n % 2 == 0 and n != 0:
#         print(f'First Even Number: {n}')
#         break
#
# print('Finished.')

# Continue Iteration
#-------------------------------------------------------
# real_money = (5, 10, 20, 50, 100, 200, 500) # EUR
# wallet = [5, 20, 10, 25, 10, 50]
#
# total = 0
# for note in wallet:
#     if note not in real_money:
#         continue
#     total += note
#
# print(f'Total: {total} EUR')

# Nested Loops
#-------------------------------------------------------
# course = [
#     ['Lesson_01.01', 'Lesson_01.02', 'Lesson_01.03', 'Lesson_01.04'],
#     ['Lesson_02.01', 'Lesson_02.02', 'Lesson_02.03'],
#     ['Lesson_03.01','Lesson_03.02', ]
# ]
#
# for module in course:
#     print(f'Starting module {module}')
#
#     for lesson in module:
#         print(f'Completed: {lesson}')
#
#     print('Module is complete!')
#     print('-------')

# for x in range(11):
#     for y in range(11):
#         for z in range(11):
#             print(x, y)

# While Loop
#---------------------------------------------------------

# count = 0
# while True:
#
#     if count == 100:
#         break
#
#     print(f'Attempt: {count}!')
#     count+=1

# Ticketing Machine Example
#---------------------------------------------------------

# tickets = 100
#
# while True:
#     n = input('Buy Tickets: ')
#     n = int(n)
#
#     if tickets - n < 0:
#         print('Not enough tickets, try again.')
#         continue
#
#     # Sell Tickets
#     tickets -= n
#     print(f'Tickets left: {tickets}')

    if tickets == 0:
        print('Sold out!')
        break