'''Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше одного раза.

Входные данные
Входная строка может содержать содержит цифры, пробелы и латинские буквы.

Выходные данные
Программа должна вывести в одну строчку в порядке возрастания все цифры,
встречающиеся во входной строке больше одного раза. Если таких цифр нет, нужно вывести слово 'NO'.'''
s = input()
b = set()
c = set()
d = set('0123456789')
for i in s:
    if i not in b and i in d:
        b.add(i)
    elif i in d:
        c.add(i)

if len(c) != 0:
    print(*sorted(c), sep='')
else:
    print('NO')