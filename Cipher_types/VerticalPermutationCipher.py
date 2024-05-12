import math


class VerticalPermutationCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, msg):
        cipher = ""
        k_indx = 0
        msg_len = float(len(msg))
        msg_lst = list(msg)
        key_lst = sorted(list(self.key))
        col = len(self.key)
        row = int(math.ceil(msg_len / col))
        fill_null = int((row * col) - msg_len)
        msg_lst.extend('_' * fill_null)
        matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]
        for _ in range(col):
            curr_idx = self.key.index(key_lst[k_indx])
            cipher += ''.join([row[curr_idx] for row in matrix])
            k_indx += 1
        return cipher

    def decrypt(self, msg):
        msgs = ""
        k_indx = 0
        msg_indx = 0
        msg_len = float(len(msg))
        msg_lst = list(msg)
        col = len(self.key)
        row = int(math.ceil(msg_len / col))
        key_lst = sorted(list(self.key))
        dec_cipher = []
        for _ in range(row):
            dec_cipher += [[None] * col]
        for _ in range(col):
            curr_idx = self.key.index(key_lst[k_indx])
            for j in range(row):
                dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                msg_indx += 1
            k_indx += 1
        try:
            msgs = ''.join(sum(dec_cipher, []))
        except TypeError:
            raise TypeError("This program cannot handle repeating words.")
        null_count = msgs.count('_')
        if null_count > 0:
            return msgs[: -null_count]
        return msgs
