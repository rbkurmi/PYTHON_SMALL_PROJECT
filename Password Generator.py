import random
import string

def password_generator(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print(f"Generated password: {password}")

password_generator(12)
