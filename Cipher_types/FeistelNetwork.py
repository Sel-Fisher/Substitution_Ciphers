class FeistelNetwork:
    def __init__(self, p, q, s, alphabet):
        self.key = self.bbs(p, q, s, 64)
        self.alphabet = alphabet

    def bbs(self, p, q, s, n):
        m = p * q
        x = (s * s) % m
        bits = ""
        for _ in range(n):
            x = (x * x) % m
            bits += str(x % 2)
        return int(bits, 2)

    def feistel_function(self, half_block, key):
        half_block_bin = format(half_block, 'b').zfill(64)
        key_bin = format(key, 'b').zfill(64)

        # XOR the half block with the key
        xor_result = int(half_block_bin, 2) ^ int(key_bin, 2)
        xor_result_bin = format(xor_result, 'b').zfill(64)

        s_box = [9, 4, 10, 11, 13, 1, 8, 5, 6, 2, 0, 3, 12, 14, 15, 7]
        s_box_output = ''
        for i in range(0, len(xor_result_bin), 4):
            s_box_output += format(s_box[int(xor_result_bin[i:i + 4], 2)], 'b').zfill(4)

        p_box = [15, 11, 7, 3, 14, 10, 6, 2, 13, 9, 5, 1, 12, 8, 4, 0]
        p_box_output = ''
        for i in p_box:
            p_box_output += s_box_output[i]

        return int(p_box_output, 2)

    def encrypt(self, message):
        message_int = int.from_bytes(message.encode(), 'big')
        left_half = message_int >> (message_int.bit_length() + 1) // 2
        right_half = message_int & ((1 << ((message_int.bit_length() + 1) // 2)) - 1)
        for _ in range(16):
            temp = right_half
            right_half = left_half ^ self.feistel_function(right_half, self.key)
            left_half = temp
        return str((left_half << ((message_int.bit_length() + 1) // 2)) + right_half)

    def decrypt(self, message):
        message = int(message)
        return message.to_bytes((message.bit_length() + 7) // 8, 'big').decode()
