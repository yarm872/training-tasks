'''Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:

Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.

Числа, стоящие выше этой диагонали, равны 0.

Числа, стоящие ниже этой диагонали, равны 2.

Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.'''
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(i):
        a[i][j] = 0
for i in range(n):
    a[n - 1 - i][i] = 1
for i in range(n):
    for j in range(n - i, n):
        a[i][j] = 2

for i in range(n):
    for j in range(n):
        print('{:1d}'.format(a[i][j]), end=' ')
    print()