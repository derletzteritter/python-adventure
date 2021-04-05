email = input("Enter your email: ").strip()

username = email[:email.index('@')]
domain = email[:email.index('@') + len(username):]

print(f"Your username is {username} and your domain is {domain}")