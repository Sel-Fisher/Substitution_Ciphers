import os

from Cipher_types.AffineCipher import AffineCipher
from Cipher_types.CaesarCipher import CaesarCipher
from Cipher_types.LinearCipher import LinearCipher


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
    choice = input("Введіть номер вибраного шифру: ")
    return choice


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
            a = int(input("Введіть коефіцієнт 'a' для лінійного шифру (окрім 1, 3, 11, 33): "))
            b = int(input("Введіть коефіцієнт 'b' для лінійного шифру: "))
            cipher = LinearCipher(a, b, alphabet)
        elif choice == "3":
            a = int(input("Введіть коефіцієнт 'a' для афінного шифру (окрім 1, 3, 11, 33): "))
            b = int(input("Введіть коефіцієнт 'b' для афінного шифру: "))
            cipher = AffineCipher(a, b, alphabet)
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
            a = int(input("Введіть коефіцієнт 'a' для розшифрування лінійного шифру (окрім 1, 3, 11, 33): "))
            b = int(input("Введіть коефіцієнт 'b' для розшифрування лінійного шифру: "))
            cipher = LinearCipher(a, b, alphabet)
        elif choice == "3":
            a = int(input("Введіть коефіцієнт 'a' для розшифрування афінного шифру (окрім 1, 3, 11, 33): "))
            b = int(input("Введіть коефіцієнт 'b' для розшифрування афінного шифру: "))
            cipher = AffineCipher(a, b, alphabet)
        else:
            print("Невірний вибір.")
            return

        input_data = get_input_data()
        if input_data is None:
            return

        input_file, output_file = input_data

        with open(input_file, "r", encoding="utf-8") as file:
            ciphertext = file.read()

        decrypted_text = cipher.decrypt(ciphertext)
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(decrypted_text)

        print("Операція завершена успішно.")

    else:
        print("Невірний вибір режиму.")
        return


if __name__ == "__main__":
    main()
