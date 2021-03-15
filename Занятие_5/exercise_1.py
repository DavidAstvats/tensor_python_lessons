'''
Вычисление факториала числа с использованием функции. 
Вводимое значение необходимо проверять и запрашивать 
ввод повторно, если введено не число.
'''
def fact(x):
    if x == 1:
        return 1
    return fact (x - 1) * x
while True:    
    fact_num = (input("Введите число для поиска факториала: "))
    try:
        fact_num = int(fact_num)
    except ValueError:
        print("Введите число!")
    else:        
        print(fact(fact_num))

