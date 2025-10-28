# Calculate Fibonacci Sequence 0 1 1 2 3 5 8 13 21 34

# Large Number Names
number_names = [
    "",
    "thousand",         # 10^3
    "million",          # 10^6
    "billion",          # 10^9
    "trillion",         # 10^12
    "quadrillion",      # 10^15
    "quintillion",      # 10^18
    "sextillion",       # 10^21
    "septillion",       # 10^24
    "octillion",        # 10^27
    "nonillion",        # 10^30
    "decillion",        # 10^33
    "bajillion"         # 10^~ (Made up)
]

a = 0
b = 1

for i in range(100):
    num             = f'{a:,d}'
    count_commas    = num.count(',')
    large_num       = number_names[count_commas]
    print(large_num, num)

    c = a + b
    a = b
    b = c
