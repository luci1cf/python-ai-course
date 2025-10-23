import random

# Rules
min_        = 1
max_        = 20
secret_num = random.randint(min_, max_)

for i in range(3):
    print(f'Attempt {i+1}/3')
    print('-'*50)
    # Ask User for Input!
    guess = input(f'Guess the secret number between {min_} and {max_}: ')
    guess = int(guess)

    # Check the Input
    if guess < min_ or guess > max_:
        print(f'Incorrect input: The number should be between {min_} and {max_}.\n')

    # Check Results
    elif guess == secret_num:
        print('Correct! You guessed it! \n')
        break

    elif guess > secret_num:
        print('Too high! Try again! \n')

    else:
        print('Too low! Try again! \n')