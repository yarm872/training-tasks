'''Напишите программу, которая переводит переданное её целое число (возможно, отрицательное) в шестнадцатеричный код. Используйте процедуру.

Входные данные
Входная строка содержит целое число N .

Выходные данные
Программа должна вывести шестнадцатеричное представление переданного её числа.'''
n=int(input())
def f(n):
    if n==0:
        return
    f(n//16)
    if n%16<10:
        print(n%16, end='')
    else:
        print(chr(n%16+55), end='')
if n==0:
    print(0)
elif n<0:
    n=-n
    print('-',end='')
    f(n)
else:
    f(n)