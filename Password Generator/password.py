import random
import string

def user_input():
    """This function handles the user input and checks whether it meets the requirements"""

    while True:
        user_length = input("Please enter the preferred length of the password (over 4): ")
        if not user_length.isdigit():
            print("Please enter a valid number.")
        elif int(user_length) <= 4:
            print("Please enter a number over 4, unless the password will be weak!")
        else:
            return int(user_length)

def password_creation(user_length):
    """This function takes the user input and generates the password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(user_length))
    return password

def main():
    user_length = user_input()
    password = password_creation(user_length)
    print(f"This is your new password: {password}\nPassword generated successfully.")

if __name__ == "__main__":
    main()



