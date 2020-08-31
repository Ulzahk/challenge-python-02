# Resolve the problem!!
import string
import random


SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
CAPITAL_LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
NUMBERS = list('0123456789')


def generate_password():
    # Start coding here
    characters = SYMBOLS + LETTERS + CAPITAL_LETTERS + NUMBERS
    password = []
    random_password_length = random.randint(12, 16)

    for i in range(random_password_length):
        random_character = random.choice(characters)
        password.append(random_character)

    password = ''.join(password)
    
    return password


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
