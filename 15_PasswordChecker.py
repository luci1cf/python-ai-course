# Is your password secure?

# Variables
#--------------------------------------------------------------------------------------
passwords = [
    "Abc%",
    "trongass9!",
    "P@2025",
    "Secure99X",
    "HelloWorld7&",
    "MyPwd2025$X",
    "Test$Pass92",
    "Abcde1#23XY",
    "UltraSafe",
    "Zz99!Xyyz"
]

# Functions
#---------------------------------------------------------------------------------------
def check_password(password):
    """ Checks the strength of the given password,

    Checks:
    - Length (mnin. 8 characters)
    - Contains at least one digit
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one special character
    - Contains no spaces

    Returns True if the password is valid, False otherwise.
    """

    print('Checking password...')

    # Placeholders
    symbols = '!@#$%^&*()_+-<>{}|[]'
    check_length = False
    check_digit = False
    check_lower = False
    check_upper = False
    check_symbol = False
    check_no_spaces = False

    # Security Checks
    # Length (min. 8 characters)
    if len(password) >= 8:
        check_length = True

    # Does not contain any spaces
    if ' ' not in password:
        check_no_spaces = True


    for char in password:
        # Contains at least one digit
        if char.isdigit():
            check_digit = True

        # Contains at least one uppercase letter
        elif char.isupper():
            check_upper = True

        # Contains at least one lowercase letter
        elif char.islower():
            check_lower = True

        # Contains at least one special character
        elif char in symbols:
            check_symbol = True

    # Display Results
    checks = [
        check_length,
        check_digit,
        check_lower,
        check_upper,
        check_symbol,
        check_no_spaces
    ]

    if all(checks):
        print('Success - Account created.')
        print('-' * 50)
        return True

    else:
        print('Password is not strong enough.')

        if not check_length:
            print('Incorrect input - Password must contain at least 8 characters.')
            print('-'*50)

        if not check_symbol:
            print(f'Incorrect input - Password must contain at least one character ({symbols}).')
            print('-' * 50)

        if not check_upper:
            print('Incorrect input - Password must contain at least one uppercase letter.')
            print('-' * 50)

        if not check_lower:
            print('Incorrect input - Password must contain at least one lowercase letter.')
            print('-' * 50)

        if not check_digit:
            print('Incorrect input - Password must contain at least one digit.')
            print('-' * 50)

        if not check_no_spaces:
            print('Incorrect input - Password must contain no spaces.')
            print('-' * 50)

# Main
#----------------------------------------------------------------------------------------
# User Input (username and password)
# print('Creating a new account')
# username = input('Username: ')
# password = input('Password: ')
# print('-'*50)

for password in passwords:
    check = check_password(password)


