import os

from Cipher_types.AffineCipher import AffineCipher
from Cipher_types.BinaryXORCipher import BinaryXORCipher
from Cipher_types.CaesarCipher import CaesarCipher
from Cipher_types.FeistelNetwork import FeistelNetwork
from Cipher_types.HashingCipher import HashingCipher
from Cipher_types.LinearCipher import LinearCipher
from Cipher_types.PlayfairCipher import PlayfairCipher
from Cipher_types.VerticalPermutationCipher import VerticalPermutationCipher
from Cipher_types.VigenerCipher import VigenereCipher

alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"


def select_cipher_mode():
    print("Виберіть режим:")
    print("1. Шифрування")
    print("2. Розшифрування")
    choice = input("Введіть номер вибраного режиму: ")
    return choice


def select_cipher():
    print("Виберіть тип шифру:")
    print("1. Шифр Цезаря")
    print("2. Лінійний шифр")
    print("3. Афінний шифр")
    print("4. Шифр Плейфера")
    print("5. Шифр Віженера")
    print("6. Шифр Вертикальної Перестановки")
    print("7: Шифр Двійкового гамування")
    print("8: Гешування")
    print("9: Мережа Фейстеля")
    choice = input("Введіть номер вибраного шифру: ")
    return choice


def select_cipher_vigenere():
    key = input("Введіть ключ для шифрування Віженера: ")
    return VigenereCipher(key, alphabet)


def select_cipher_playfair():
    key = input("Введіть ключ для шифрування Плейфера: ")
    return PlayfairCipher(key, alphabet)


def select_cipher_binary_xor():
    seed = int(input("Введіть початкове значення для шифру Двійкового гамування: "))
    p = int(input("Введіть просте число 'p' для генератора Блюм-Блюм-Шуба: "))
    q = int(input("Введіть просте число 'q' для генератора Блюм-Блюм-Шуба: "))
    return BinaryXORCipher(seed, p, q)


def select_cipher_feistel():
    p = int(input("Введіть просте число 'p' для генерації ключа BBS: "))
    q = int(input("Введіть просте число 'q' для генерації ключа BBS: "))
    s = int(input("Введіть початкове значення для шифру BBS: "))
    cipher = FeistelNetwork(p, q, s, alphabet=alphabet)
    return cipher


def get_input_data():
    input_file = input("Введіть ім'я вхідного файлу: ")
    if not os.path.exists(input_file):
        print("Вхідний файл не знайдено.")
        return None

    output_file = input("Введіть ім'я вихідного файлу: ")

    return input_file, output_file


def main():
    mode = select_cipher_mode()

    if mode == "1":
        choice = select_cipher()

        if choice == "1":
            shift = int(input("Введіть зсув для шифру Цезаря: "))
            cipher = CaesarCipher(shift, alphabet)
        elif choice == "2":
            a = int(input("Введіть коефіцієнт 'a' для лінійного шифру: "))
            b = int(input("Введіть коефіцієнт 'b' для лінійного шифру: "))
            cipher = LinearCipher(a, b, alphabet)
        elif choice == "3":
            a = int(input("Введіть коефіцієнт 'a' для афінного шифру: "))
            b = int(input("Введіть коефіцієнт 'b' для афінного шифру: "))
            cipher = AffineCipher(a, b, alphabet)
        elif choice == "4":
            cipher = select_cipher_playfair()
        elif choice == "5":
            cipher = select_cipher_vigenere()
        elif choice == "6":
            key = input("Введіть ключ для шифрування Вертикальної Перестановки: ")
            cipher = VerticalPermutationCipher(key)
        elif choice == "7":
            cipher = select_cipher_binary_xor()
        elif choice == "8":
            cipher = HashingCipher()
        elif choice == "9":
            cipher = select_cipher_feistel()
        else:
            print("Невірний вибір.")
            return

        input_data = get_input_data()
        if input_data is None:
            return

        input_file, output_file = input_data

        with open(input_file, "r", encoding="utf-8") as file:
            plaintext = file.read()

        encrypted_text = cipher.encrypt(plaintext)
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(encrypted_text)

        print("Операція завершена успішно.")

    elif mode == "2":
        choice = select_cipher()

        if choice == "1":
            shift = int(input("Введіть зсув для розшифрування Цезаря: "))
            cipher = CaesarCipher(shift, alphabet)
        elif choice == "2":
            a = int(input("Введіть коефіцієнт 'a' для розшифрування лінійного шифру: "))
            b = int(input("Введіть коефіцієнт 'b' для розшифрування лінійного шифру: "))
            cipher = LinearCipher(a, b, alphabet)
        elif choice == "3":
            a = int(input("Введіть коефіцієнт 'a' для розшифрування афінного шифру: "))
            b = int(input("Введіть коефіцієнт 'b' для розшифрування афінного шифру: "))
            cipher = AffineCipher(a, b, alphabet)
        elif choice == "4":
            cipher = select_cipher_playfair()
        elif choice == "5":
            cipher = select_cipher_vigenere()
        elif choice == "6":
            key = input("Введіть ключ для розшифрування Вертикальної Перестановки: ")
            cipher = VerticalPermutationCipher(key)
        elif choice == "7":
            cipher = select_cipher_binary_xor()
        elif choice == "8":
            print("Геш неможливо розшифрувати, але ми можемо перевірити чи геш вхідного файлу дорівнює вихідному файлу")
            cipher = HashingCipher()
            input_file, output_file = get_input_data()
            with open(input_file, "r", encoding="utf-8") as file:
                plain_text = file.read()
            check_hash = cipher.encrypt(plain_text)
            with open(output_file, "r", encoding="utf-8") as file:
                existing_hash = file.read()
            if check_hash == existing_hash:
                print("Геш вхідного файлу дорівнює гешу вихідного файлу")
                return
            else:
                print("Геш вхідного файлу відрізняється від гешу вихідного файлу")
                return
        elif choice == "9":
            cipher = FeistelNetwork(1, 1, 1, alphabet=alphabet)
        else:
            print("Невірний вибір.")
            return

        input_data = get_input_data()
        if input_data is None:
            return

        input_file, output_file = input_data

        with open(input_file, "r", encoding="utf-8") as file:
            plaintext = file.read()

        decrypted_text = cipher.decrypt(plaintext)
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(decrypted_text)

        print("Операція завершена успішно.")


if __name__ == "__main__":
    main()
