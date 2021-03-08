import random
def xor_encryption():

    while True:
        a = input("Specify the location of a file. The results will be written there: ")
        def read_file(filename = a):
            x_file = open(filename, 'rb')
            inf = x_file.read()
            x_file.close()
            return inf

        def write_file(inf, filename = a):
            x_file = open(filename, 'wb')
            x_file.write(inf)
            x_file.close()

        try:
            text = input("Type something... or press \"Enter\" to take the text from the file: ")
            if not text:
                text = read_file()
        except PermissionError:
            print("Permission denied! Not enough rights to work with the file.")
            continue
        except FileNotFoundError:
            print("invalid file identifier (no such file or directory).")
            continue
        except:
            print("Unknown error.")
            continue
        key = input("Enter the key or press \"Enter\" for the key to be generated automatically: ")
        if not key:
            key = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") for i in range(random.randint(1, len(text))))
            print(f"The key was created automatically:{key}")
        xor_code_result = bytearray()
        if type(text) == str:
            text = bytearray(text, "utf-8")
        key = bytearray(key, "utf-8")
        for i in range(len(text)):
            xor_code_result.append(text[i] ^ key[i % len(key)])
        try:
            write_file(xor_code_result)
            print("The result is written in the file")
            break
        except PermissionError:
            print("Not enough rights to work with the file.")
            continue
        except:
            print("Unknown error.")
            continue

def frequency_of_using_digits():
    while True:
        try:
            a = int(input("Enter first number: "))
            break
        except ValueError:
            print("You entered an invalid value!")
            continue

    while True:
        try:
            b = int(input("Enter second number: "))
            break
        except ValueError:
            print("Negative numbers cannot be entered.")
            continue

    freq_tuple = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for number in range(a,b + 1):
            string = str(number)
            for i in range(len(string)):
                freq_tuple[int(string[i])] += 1
    for i in range(len(freq_tuple)):
        print(f'{i}:{freq_tuple[i]}')

def freq_of_using_symbols_in_the_text():
    while True:
        a = input("Specify the location of a file. The text will be taken from there \nPress \"Enter\" for continue without file: ")
        def read_file(filename = a): 
            x_file = open(filename, 'rb')
            inf = x_file.read()
            x_file.close()
            return inf
        
        try:
            text = input("Type some text \nOr press \"Enter\" for reading from a file: ")
            if a:
                text = read_file().decode()
            elif not a and not text:
                print("No data")
                continue
        except PermissionError:
            print("Permission denied! Not enough rights to work with the file.")
            continue
        except FileNotFoundError:
            print("invalid file identifier (no such file or directory).")
            continue
        except:
            print("Unknown error.")
            continue
        fq = {}
        for symbol in text:
            if fq.get(symbol):
                fq[symbol] += 1
            else:
                fq[symbol] = 1

        for key in sorted(fq):
            print(f'{key}: {fq[key]}')

while True:
    choose = input(
"""
Select operation:
1. XOR encryption.
2. The frequency of using digits in a range of numbers.
3. The frequency of using symbols in the text.
|||Enter "exit" for leave from program|||
"""        
    )
    if choose == "1":
        print("You have selected operation \"1\"")
        xor_encryption()
    elif choose == "2":
        print("You have selected operation \"2\"")
        frequency_of_using_digits()
    elif choose == "2":
        print("You have selected operation \"3\"")
        freq_of_using_symbols_in_the_text()
    elif choose == "exit":
        print("Good Bye!")
        break