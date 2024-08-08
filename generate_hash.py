import bcrypt

password = b"your_new_password"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed.decode())
