def email_slicer():
    email = input("Enter your email address: ").strip()
    username, domain = email.split('@')
    print(f"Username: {username}")
    print(f"Domain: {domain}")

email_slicer()
