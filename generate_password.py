from werkzeug.security import generate_password_hash

password = input("Enter your admin password: ")
hashed_password = generate_password_hash(password)
print("Your hashed password is:")
print(hashed_password)
