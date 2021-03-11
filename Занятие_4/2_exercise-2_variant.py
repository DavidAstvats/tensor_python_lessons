'''

2 Задание. (свой вариант)
Даны два списка. Определите разницу между элементами списках.

'''

def difference(list_1, list_2):
    return list(set(list_1).symmetric_difference(list_2))

#Наглядный пример.
a = [1, 2, 3]
b = [1, 2, 3, 4, 5]

print(difference(a, b))