class CaesarCipher:
    def __init__(self, shift, alphabet):
        self.shift = shift
        self.alphabet = alphabet

    def encrypt(self, plaintext):
        encrypted_text = ""
        for char in plaintext:
            if char.upper() in self.alphabet:
                if char.islower():
                    index = (self.alphabet.index(char.upper()) + self.shift) % len(self.alphabet)
                    encrypted_text += self.alphabet[index].lower()
                else:
                    index = (self.alphabet.index(char) + self.shift) % len(self.alphabet)
                    encrypted_text += self.alphabet[index]
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = ""
        for char in ciphertext:
            if char.upper() in self.alphabet:
                if char.islower():
                    index = (self.alphabet.index(char.upper()) - self.shift) % len(self.alphabet)
                    decrypted_text += self.alphabet[index].lower()
                else:
                    index = (self.alphabet.index(char) - self.shift) % len(self.alphabet)
                    decrypted_text += self.alphabet[index]
            else:
                decrypted_text += char
        return decrypted_text
