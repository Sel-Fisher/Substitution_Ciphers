class VigenereCipher:
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.key_length = len(key)
        self.alphabet_length = len(alphabet)

    def encrypt(self, message):
        encrypted_message = ""
        original_case = [char.islower() for char in message]
        message = message.upper()
        for i in range(len(message)):
            if message[i] not in self.alphabet:
                encrypted_message += message[i]
                continue
            key_character = self.key[i % self.key_length]
            message_character = message[i]
            new_character_index = (self.alphabet.index(message_character) + self.alphabet.index(
                key_character)) % self.alphabet_length
            encrypted_message += self.alphabet[new_character_index]
        return "".join([char.lower() if is_lower else char for char, is_lower in zip(encrypted_message, original_case)])

    def decrypt(self, message):
        decrypted_message = ""
        original_case = [char.islower() for char in message]
        message = message.upper()
        for i in range(len(message)):
            if message[i] not in self.alphabet:
                decrypted_message += message[i]
                continue
            key_character = self.key[i % self.key_length]
            message_character = message[i]
            new_character_index = (self.alphabet.index(message_character) - self.alphabet.index(
                key_character)) % self.alphabet_length
            decrypted_message += self.alphabet[new_character_index]
        return "".join([char.lower() if is_lower else char for char, is_lower in zip(decrypted_message, original_case)])
