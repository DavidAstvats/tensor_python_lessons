'''
Написать программу подсчета частоты вхождений 
символов в текст с использованием lambda.
'''

from collections import Counter

count = lambda symbol: Counter(symbol)
symbol = input("Вставьте сюда или введите какой-нибудь текст:\n")

print(f'Подсчет символов:\n{count(symbol)}')
