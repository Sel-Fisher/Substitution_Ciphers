import hashlib


class HashingCipher:
    def encrypt(self, message):
        sha1 = hashlib.sha1()
        sha1.update(message.encode())
        return sha1.hexdigest()
