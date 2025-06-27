import hashlib

res = open("top-10000-passwords.txt").read().split("\n")

def crack_sha1_hash(hash, use_salts = False):
    for i in range(10000):
        hash_c = hashlib.sha1(res[i].encode('latin-1')).hexdigest()
        if hash == hash_c:
            return res[i]
    return 'PASSWORD NOT IN DATABASE'
