import sys
import string
from random import choice
from time import sleep

def title(msg=''):
    print("=" * 50)
    print(msg.center(50))
    print("=" * 50)

def get_character_set():
    character_set = string.ascii_letters + string.digits + string.punctuation
    return character_set


def get_password_length(length=8):
    try:
        password_length = int(input(f"Password length (default is {length}): "))
    except:
        password_length = length
    return password_length


def generate_password(length):
    password = ''.join(choice(get_character_set())for _ in range(length))
    return f"Your password: {password}"


def main():
    title("PASSWORD GENERATOR v1.1")

    while True:
        length = get_password_length()
        password = generate_password(length)
        print("Generating your password...")
        sleep(1)
        print(password)
        sleep(1)

        new_password = None

        while new_password != 'y':
            new_password = str(input("Do you want generate a new password? [y/N]: ")).strip()[0]

            if new_password.lower() != 'y':
                title("EXIT PROGRAM...")
                sleep(1)
                sys.exit()


if __name__ == "__main__":
    main()
