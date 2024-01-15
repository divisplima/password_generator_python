import sys
import string
from random import choice
from time import sleep

colours_code = {
    'clean': '\033[0m',
    'underscode' : '\033[4m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m'
}

def title(msg=''):
    print(colours_code['red'] + "=" * 50)
    print(msg.center(50))
    print("=" * 50 + colours_code['clean'])


def password_type():
    print(f"{colours_code['yellow']}Define your password type:\n[1] - Numeric\n[2] - Alphanumeric\n[3] - Alphanumeric with Punctuation{colours_code['clean']}")
    while True:
        try:
            option = int(input(f"{colours_code['yellow']}{colours_code['underscode']}Your option{colours_code['clean']}: "))
            if option in [1, 2, 3]:
                break
            else:
                print(f"{colours_code['red']}Insert a valid number.{colours_code['clean']}")
        except ValueError:
            print(f"{colours_code['red']}Insert a valid number.{colours_code['clean']}")
    return option


def get_character_set(option):
    match option:
        case 1:
            character_set = string.digits
        case 2:
            character_set = string.digits + string.ascii_letters
        case 3:
            character_set = string.digits + string.ascii_letters + string.punctuation
    return character_set


def get_password_length(length=8):
    try:
        password_length = int(input(f"{colours_code['yellow']}{colours_code['underscode']}Password length (default is {length}){colours_code['clean']}: "))
    except ValueError:
        password_length = length
    return password_length


def generate_password(length, character_set):
    password = ''.join(choice(character_set) for _ in range(length))
    return f"{colours_code['yellow']}Your password: {colours_code['green']}{password}{colours_code['clean']}"


def main():
    while True:
        title(f"PASSWORD GENERATOR v1.2")
        option = password_type()
        character_set = get_character_set(option)
        length = get_password_length()
        password = generate_password(length, character_set)

        print(f"{colours_code['green']}Generating your password...{colours_code['clean']}")
        sleep(1)
        print(password)
        sleep(1)

        new_password = str(input(f"{colours_code['yellow']}Do you want to generate a new password? [y/N]: {colours_code['clean']}")).strip().lower()[0]

        if new_password != 'y':
            print(f"{colours_code['red']}Exiting program...{colours_code['clean']}")
            sleep(1)
            sys.exit()


if __name__ == "__main__":
    main()
