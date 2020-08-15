import hashlib
a = "password"
r = hashlib.md5(a.encode())
print(r.hexdigest())
