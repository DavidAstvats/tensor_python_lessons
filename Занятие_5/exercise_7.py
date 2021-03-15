'''
Вычисление факториала числа с использованием lambda (рекурсия).
'''

def fact():
    fact_num = int(input("Введите число для поиска факториала: "))
    factorial = lambda f: f * factorial(f-1) if f > 0 else 1

    print(factorial(fact_num))

fact()
