class LinearCipher:
    def __init__(self, a, b, alphabet):
        self.a = a
        self.b = b
        self.alphabet = alphabet

    def encrypt(self, plaintext):
        encrypted_text = ""
        for char in plaintext:
            if char.upper() in self.alphabet:
                if char.islower():
                    index = (self.a * self.alphabet.index(char.upper()) + self.b) % len(self.alphabet)
                    encrypted_text += self.alphabet[index].lower()
                else:
                    index = (self.a * self.alphabet.index(char) + self.b) % len(self.alphabet)
                    encrypted_text += self.alphabet[index]
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = ""
        for char in ciphertext:
            if char.upper() in self.alphabet:
                if char.islower():
                    index = self.mod_inverse(self.a, len(self.alphabet)) * (self.alphabet.index(char.upper()) - self.b) % len(self.alphabet)
                    decrypted_text += self.alphabet[index].lower()
                else:
                    index = self.mod_inverse(self.a, len(self.alphabet)) * (self.alphabet.index(char) - self.b) % len(self.alphabet)
                    decrypted_text += self.alphabet[index]
            else:
                decrypted_text += char
        return decrypted_text

    def mod_inverse(self, a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None
