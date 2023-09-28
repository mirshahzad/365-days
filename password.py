# Importing library
import hashlib

# Defining funciton with "has_password" as a name
def hash_password(password):
    # Encode the password as bytes
    password_bytes = password.encode('utf-8')
    
    # Use SHA-256 hash function to create a hash object
    hash_object = hashlib.sha256(password_bytes)
    
    # Get the hexadecimal representation of the hash
    password_hash = hash_object.hexdigest()
    
    return password_hash

# In the output display, you have to input the password
password = input("Input your password: ")
hashed_password = hash_password(password)
print(f"Your 256 hashed password is: {hashed_password}")