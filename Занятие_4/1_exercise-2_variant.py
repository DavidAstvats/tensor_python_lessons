'''
1 Задание.
Реализация алгоритма сортировки списка/массива пузырьковым методом.
2 Вариант как программа, которая запрашивает какие числа нужно отсортировать
'''

unsorted_list = []
number = int(input("Введите длину списка: "))
print("Введите числа: ")
for i in range(number):
    data = int(input())
    unsorted_list.append(data)

def bubble_sort(my_list):
    last_item = len(my_list) - 1
    for z in range(0, last_item):
        for x in range(0, last_item - z):
            print(my_list)
            if my_list[x] > my_list[x+1]:
                my_list[x], my_list[x+1] = my_list[x+1], my_list[x]

    return my_list

print("Несортированный список:", unsorted_list)
sorted_list = bubble_sort(unsorted_list).copy()
print("Сортированный список:", sorted_list)
