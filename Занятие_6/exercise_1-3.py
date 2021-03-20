"""
1. XOR шифрование, на входе файл с текстом и ключ шифрования (строка), на выходе
зашифрованное сообщение в файле.
2. XOR расшифровывание, на входе зашифрованное сообщение в файле и ключ (строка),
на выходе исходный текст в файле.
3. Необходимо реализовать предыдущие 2 задания с использованием менеджера контекста
with … as.
"""

import random

def read_file(road_to_file):
    with open(road_to_file, "rb") as f:
        f = f.read()
        return f

    
def write_file(road_to_file, xor_code):
    with open(road_to_file, "wb") as f:
        f.write(xor_code)

road_to_file = ""
text = ""
print("XOR - шифрование")
while road_to_file !="выход":
    print("Введите \"выход\" - для выхода.")
    road_to_file = input("Введите путь к файлу:\n")
    if road_to_file != "выход":
        try:
            text = input("Введите текст (Enter - текст будет взят из файла):")
            if not text:
                text = read_file(road_to_file)
        except PermissionError:
            print("Недостаточно прав для работы с файлом.")
            continue
        except FileNotFoundError:
            print("Неверный путь к файлу или такого файла не существует.")
            continue
        except:
            print("Неизвестная ошибка")
            continue
        key = input("Введите ключ (Enter - ключ будет создан автоматически):")
        if not key:
            key = "".join(random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") for i in range(random.randint(1, len(text))))
            print(f"Ключ был создан автоматически:{key}")
        xor_code = bytearray()
        if type(text) == str:
            text = bytearray(text, "utf-8")
        key = bytearray(key, "utf-8")
        for i in range(len(text)):
            xor_code.append(text[i] ^ key[i % len(key)])
        try:
            write_file(road_to_file, xor_code)
            print("Результат записан в файл")
        except PermissionError:
            print("Недостаточно прав для работы с файлом.")
            continue
        except:
            print("Неизвестная ошибка")
            continue
