'''Напишите программу, которая находит в массиве количество элементов, равных максимальному.

Входные данные
Первая строка содержит размер массива N . Во второй строке через пробел задаются N чисел – элементы массива. Гарантируется, что 0< N ≤10000 .

Выходные данные
Программа должна вывести два числа, разделив их пробелом: максимальный элемент массива и количество элементов массива, равных максимальному.'''
n=int(input())
a=list(map(int,input().split()))
ma=a[0]
s=1
for i in range(1,len(a)):
    if a[i]>ma:
        ma=a[i]
        s=1
    elif a[i]==ma:
        s+=1
print(ma,end=' ')
print(s)