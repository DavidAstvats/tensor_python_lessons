print("""
Вводите ваш запрос в следующем виде:
"цифра_*|пробел|*_операция_*|пробел|*_цифра"
Пример: 5 + 5
Операции: 
Сложение - "+"   
Вычитание - "-"  
Умножение - "*"  
Деление - "/"  
Возведение в степень - "**" 
Остаток от деления - "%" """)

def calc(a=1, b=2, operation=" "):
    def addition(a1, b1):
        return a1 + b1

    def subtraction(a1, b1):
        return a1 - b1

    def multiply(a1, b1):
        return a1 * b1

    def divide(a1, b1):
        return a1 / b1

    def exponentiation(a1, b1):
        return a1 ** b1
    
    def remainder_division(a1, b1):
        return a1 % b1

    selector = {
        "+": addition,
        "-": subtraction,
        "*": multiply,
        "/": divide,
        "**": exponentiation,
        "%": remainder_division
        }

    return selector[operation](a, b)


num = True
while num:
    num = input("""
При пустом поле для ввода нажмите "Enter" для выхода. 
Введите значение: """)
    if num:
        ls = list(num.split())
        try:
            ls[0] = float(ls[0])
            ls[2] = float(ls[2])
        except ValueError:
            print("Проверьте правильность ввода.")
            continue
        except OverflowError:
            print("Числа слишком большие.")
            continue
        except IndexError:
            print("Проверьте правильность ввода согласно инструкции.")
            continue
        if len(ls) == 3:
            if ls[1] == "+" or ls[1] == "-" or ls[1] == "*" or ls[1] == "/" or ls[1] == "**"  or ls[1] == "%":
                try:
                    answer = calc(ls[0], ls[2], ls[1])
                except ZeroDivisionError:
                    print(f"{ls[0]} {ls[1]} {ls[2]} = Результат стремится к бесконечности.")
                except OverflowError:
                    print("Переполнение.")
                else:
                    print(f"{ls[0]} {ls[1]} {ls[2]} = {answer:.3f}")
            else:
                print("Неверно заданная операция.")
                continue
        else:
            print("Проверьте правильность ввода согласно инструкции.")
            continue
    else:
        print("Удачи.")