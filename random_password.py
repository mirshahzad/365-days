# Importing random and string module from python libraries
import random
import string

# Defining function
def generate_password(length=8):
    # Define the characters to use in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # use the random module to generate the password
    password = ''.join(random.choice(all_characters) for  i in range (length))

    return password

password_length_str = input("Write the length of your password:")
if password_length_str:
    password_length = int(password_length_str)
else:
    password_length = 8

password = generate_password(password_length)
print(f"Here is your random password with a length you provided, if you didn't provide the length, the default length is 8 characaters: {password}")