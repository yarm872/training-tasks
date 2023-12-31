'''Напишите программу, которая строит алфавитно-частотный словарь для файла input.txt , в котором в столбик записаны
слова, состоящие только из строчных букв латинского алфавита. Слова нужно отсортировать в порядке убывания частоты
(сначала слова, которые встретились чаще всего). Слова с одинаковой частотой должны располагаться в алфавитном порядке.

Входные данные
Входной файл содержит неизвестное количество строк, в каждой из которых записано слово, состоящее только из строчных
букв латинского алфавита. Последняя строка файла – пустая.

Выходные данные
Программа должна вывести в файл output.txt все различные слова, которые встретились исходном файле, по одному слову в
строке. После каждого слова через пробел записывается количество таких слов в файле. Слова должны быть отсортированы по
убыванию частоты (сначала слова, которые встретились чаще всего). Слова с одинаковой частотой должны располагаться в
алфавитном порядке.'''
f = open('input.txt')
fout = open('output.txt', 'w')
d = {}
while True:
    s = f.readline()
    if not s:
        break
    s = s.strip()
    s = s.split()
    for g in s:
        d[g] = d.get(g, 0) + 1

sp = []
for i in d:
    sp.append((-d[i], i))
sp.sort()
for i in range(len(sp)):
    print(sp[i][1], -sp[i][0], file=fout)
f.close()
fout.close()