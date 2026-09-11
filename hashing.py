# Hashing: one way function. Same input --> same output. 

import hashlib

password = "monkey200"

data = password.encode("utf-8")
digest = hashlib.md5(data).hexdigest()

print(f"Password: {password}")
print(f"Hash: {digest}")




diff_passwords = ["monkey100", "monkey200", "monkey300", "monkey400", "monkey500"]
for p in diff_passwords:
    diff_data = p.encode("utf-8")
    diff_digest = hashlib.sha256(diff_data).hexdigest()

    print(f"Pasword: {p}")
    print(f"Hash: {diff_digest}", "\n")