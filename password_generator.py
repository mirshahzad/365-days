# Password Generator program

# Importing Secrets module which used for generating cryptographically
# strong random numbers suitable for managing data such as passwords, 
# account authentication, security tokens, and related secrets.
import secrets
import string

# Defining a function named create_pw with maximum length of 8 characters.
def create_pw(pw_length=8):
   letters = string.ascii_letters
   digits = string.digits
   special_chars = string.punctuation

   alphabet = letters + digits + special_chars
   pwd = ''
   pw_strong = False

   while not pw_strong:
       pwd = ''
       for i in range(pw_length):
           pwd += ''.join(secrets.choice(alphabet))

       if (any(char in special_chars for char in pwd) and
               sum(char in digits for char in pwd) >= 2):
           pw_strong = True

   return pwd


if __name__ == '__main__':
   print(create_pw())