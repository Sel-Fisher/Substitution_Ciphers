class PlayfairCipher:
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet + '.,_'

    def _generate_playfair_table(self):
        table = [['' for _ in range(6)] for _ in range(6)]
        key_index = 0
        used_letters = set()

        # Fill in the table with the key
        for i in range(6):
            for j in range(6):
                while key_index < len(self.key) and self.key[key_index].upper() in used_letters:
                    key_index += 1
                if key_index < len(self.key):
                    char = self.key[key_index].upper()
                    key_index += 1
                else:
                    char = self._get_next_unused_letter(used_letters)
                table[i][j] = char
                used_letters.add(char)

        return table

    def _get_next_unused_letter(self, used_letters):
        for char in self.alphabet:
            if char not in used_letters and char != 'Й':
                return char
        return ''

    def _prepare_input(self, plaintext):
        # Remove spaces and replace J with I
        plaintext = plaintext.upper().replace('Й', 'І').replace(' ', '')
        # Break plaintext into digraphs
        digraphs = []
        i = 0
        while i < len(plaintext):
            if i == len(plaintext) - 1 or plaintext[i] == plaintext[i + 1]:
                digraphs.append(plaintext[i] + 'Х')
                i += 1
            else:
                digraphs.append(plaintext[i] + plaintext[i + 1])
                i += 2
        return digraphs

    def _find_position(self, table, char):
        for i in range(6):
            for j in range(6):
                if table[i][j] == char:
                    return i, j
        return -1, -1

    def encrypt(self, plaintext):
        table = self._generate_playfair_table()
        digraphs = self._prepare_input(plaintext)
        ciphertext = []

        for digraph in digraphs:
            char1, char2 = digraph[0], digraph[1]
            row1, col1 = self._find_position(table, char1)
            row2, col2 = self._find_position(table, char2)

            if row1 == row2:  # Same row
                ciphertext.append(table[row1][(col1 + 1) % 6] + table[row2][(col2 + 1) % 6])
            elif col1 == col2:  # Same column
                ciphertext.append(table[(row1 + 1) % 6][col1] + table[(row2 + 1) % 6][col2])
            else:  # Forming a rectangle
                ciphertext.append(table[row1][col2] + table[row2][col1])

        return ''.join(ciphertext)

    def decrypt(self, ciphertext):
        table = self._generate_playfair_table()
        digraphs = self._prepare_input(ciphertext)
        plaintext = []

        for digraph in digraphs:
            char1, char2 = digraph[0], digraph[1]
            row1, col1 = self._find_position(table, char1)
            row2, col2 = self._find_position(table, char2)

            if row1 == row2:  # Same row
                plaintext.append(table[row1][(col1 - 1) % 6] + table[row2][(col2 - 1) % 6])
            elif col1 == col2:  # Same column
                plaintext.append(table[(row1 - 1) % 6][col1] + table[(row2 - 1) % 6][col2])
            else:  # Forming a rectangle
                plaintext.append(table[row1][col2] + table[row2][col1])

        return ''.join(plaintext).replace('Х', '')
