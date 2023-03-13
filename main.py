import bcrypt

password = "Luke1579"
bytes = password.encode("utf-8")
salt = bcrypt.gensalt()
hash = bcrypt.hashpw(bytes, salt)

print(bytes, salt, hash)

result = bcrypt.checkpw("Luke1579".encode(), hash)

print(result)