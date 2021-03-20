'''
3 задание. (свой вариант)
Выявление элемента в списке, повторяющегося чаще всего
'''

from collections import Counter

numbers = [1, 2, 3, 4, 4, 4, 5, 6, 6]

def most_common(list):
    data = Counter(list)
    return data.most_common(1)[0][0]
 
print(most_common(numbers))
