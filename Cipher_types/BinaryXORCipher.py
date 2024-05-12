class BinaryXORCipher:
    def __init__(self, seed, p, q):
        self.seed = seed
        self.p = p
        self.q = q
        self.modulus = p * q

    def bbs_generator(self):
        x = (self.seed**2) % self.modulus
        while True:
            x = (x**2) % self.modulus
            yield x & 1

    def encrypt(self, message):
        generator = self.bbs_generator()
        encrypted = "".join(chr(ord(c) ^ next(generator)) for c in message)
        return encrypted

    def decrypt(self, message):
        return self.encrypt(message)
