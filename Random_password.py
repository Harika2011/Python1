#Write a Python program to generate a random password consisting of lower case and upper case characters along with numbers. 
# You can also use random module for shuffling the password generated.


import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
    ]
    
    all_characters = lower + upper + digits
    password += random.choices(all_characters, k=length - 3)
    
    random.shuffle(password)
    
    return ''.join(password)

password = generate_password(12)
print("Generated password:", password)
