'''
Удалить из списка элементы, значения которых 
уже всречались в этом же списке в предыдущих элементах.
'''

x = ['a','a','b','b','c','k','k']

for z in x:
    while x.count(z) > 1:
        x.remove(z)
print(x)
