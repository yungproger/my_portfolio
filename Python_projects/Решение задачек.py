# 1 задача
from Tools.scripts.make_ctype import values

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for b in a:
    if b < 5:
        print(b)

# 2 задача

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = list(filter(lambda elem: elem in a, b))
print(result)

# 3 задача

import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
result1 = dict(sorted(d.items(), key=operator.itemgetter(1)))
result2 = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(result1)
print(result2)

# 4 задача

dict_a = {1: 10, 10: 100}
dict_b = {5: 50, 7: 70}

result3 = {**dict_a, **dict_b}  # Объединение словарей
print(result3)

# 5 задача

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
result4 = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# Найдено 3 ключа с самым высоким значением с помощью функции sorted.
print(result4)

# 6 задача

# Rод, который переводит целое число в строку, при том что его можно применить в любой системе счисления.
print(int('ABC', 16))


# 7 задача

# Нужно вывести первые n строк треугольника Паскаля.
def pascal_triangle(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]


pascal_triangle(5)

# 8 задача

# Напишите проверку на то, является ли строка палиндромом.

word = str(input('Введите слово '))
if word == ''.join(reversed(word)):
    print('Введенное слово - палиндром')
else:
    print("Введенное слово - не палиндром")

# 9 задача
# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

def convert(seconds):
    days = seconds // (24*3600)
    hours = seconds // 3600
    minutes = seconds // 60
    seconds = seconds // 1
    print(f'{days},{hours},{minutes},{seconds}')
convert(123455)

# 10 задача
# Вы принимаете от пользователя последовательность чисел, разделённых запятой.
# Составьте список и кортеж с этими числами.

numbers = input('Введите последовательность чисел, разделённых запятой: ')
converts_int = numbers.split(',')
ints = map(int, converts_int)
lst = list(ints)
tup = tuple(lst)
print('Список: ', lst)
print('Кортеж: ', tup)










