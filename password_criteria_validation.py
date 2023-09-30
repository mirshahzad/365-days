# Importing Regular Expression python library
import re

# Defining function
def validate_password(password):
    
    # Check if the password has atleast 8 characters
    if len(password) < 8:
        return False
    
    # Check if the password contains atleast one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check if the password containt atleast one digit
    if not re.search(r'\d', password):
        return False
    
    # Check if the password containt atleast one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    # If all the conditions are met, the password is valid
    return True

# Print message
password = input("Write your password: ")
is_valid = validate_password(password)

if is_valid:
    print ("The password is valid!")
else: print("The password does not meet the requirements.")