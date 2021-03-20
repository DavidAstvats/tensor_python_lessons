'''
1 Задание.
Реализация алгоритма сортировки списка/массива пузырьковым методом.
1 Вариант.
'''

unsorted_list = [30, 83, -16, 4, 125, 40, -13]

def bubble_sort(my_list):
    last_item = len(my_list) - 1
    for z in range(0, last_item):
        for x in range(0, last_item - z):
            print(my_list)
            if my_list[x] > my_list[x+1]:
                my_list[x], my_list[x+1] = my_list[x+1], my_list[x]

    return my_list

print("Unsorted list: ", unsorted_list)
sorted_list = bubble_sort(unsorted_list).copy()
print("Sorted list", sorted_list)
