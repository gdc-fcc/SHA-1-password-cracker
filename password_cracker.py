import hashlib

passwords = open("top-10000-passwords.txt").read().split("\n")
salts = open("known-salts.txt").read().split("\n")

def hash1(password):
    return hashlib.sha1(password.encode()).hexdigest()

def crack_sha1_hash(hash, use_salts = False):
    for password in passwords:
        if hash == hash1(password):
            return password
    if use_salts:
        for password in passwords:
            for salt in salts:
                if hash == hash1(salt + password):
                    return password
                if hash == hash1(password+salt):
                    return password
    return 'PASSWORD NOT IN DATABASE'
