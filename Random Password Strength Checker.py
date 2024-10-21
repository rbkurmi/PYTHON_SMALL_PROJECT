import re

def password_strength_checker(password):
    if len(password) < 6:
        return "Weak"
    elif re.search("[a-zA-Z]", password) and re.search("[0-9]", password):
        return "Medium"
    elif re.search("[a-zA-Z]", password) and re.search("[0-9]", password) and re.search("[!@#$%^&*()]", password):
        return "Strong"
    else:
        return "Weak"

password = input("Enter a password: ")
strength = password_strength_checker(password)
print(f"Password strength: {strength}")
