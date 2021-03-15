'''
Вычисление факториала числа 
с использованием lambda (не рекурсия)
'''
import math

a = lambda x: math.factorial(x)

while True:
    x = input('Введите число: ')
    try:
        x = int(x)
        break
    except ValueError:
        print('Неверно заданное значение!')
print(f'{x}! = {a(x)}')
