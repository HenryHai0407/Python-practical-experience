# setting up
import random
import string

letters = string.ascii_letters
digits = string.digits
special_characters = string.punctuation

# print(special_characters)
# function to generate random password

def password_length():
    length = input("Enter the length of the password: ")
    return int(length)

def generate_password(length=10):
    all_characters = f"{letters}{digits}{special_characters}"
    all_characters_list = list(all_characters)
    random.shuffle(all_characters_list)
    random_password = random.choices(all_characters_list, k=length)
    random_password = "".join(random_password)
    return random_password

def main():
    length1 = password_length()
    password = generate_password(length1)
    print(password)

if __name__ == "__main__":
    main()
