'''Напишите программу, которая определяет, можно ли переставить английские буквы введённого предложения
(не учитывая остальные символы) так, чтобы получить палиндром -– слово, которое читается одинаково слева направо и
справа налево. Строчные и прописные буквы не различаются. Символы, не являющиеся английскими буквами, не учитываются.
Если это сделать нельзя, программа должна вывести на экран слово «NO», а если можно – искомое слово прописными буквами.
Если таких слов несколько, нужно вывести последнее в алфавитном порядке слово.

Входные данные
На вход программу подаётся символьная строка, содержащая произвольные символы.

Выходные данные
Если можно переставить английские буквы введённого предложения, так, чтобы получить палиндром, программа должна вывести
этот палиндром прописными буквами. Если это сделать нельзя, программа должна вывести слово «NO».'''
d={}
a=input().upper()
for i in a:
    if 'A'<=i<='Z':
        d[i]=d.get(i,0)+1
t=0
f=''
for i in d.keys():
    if d[i]%2:
        f=i
        t+=1
        if t>1:
            print('NO')
            exit()
s=''
for i in reversed(sorted(d)):
    s+=i*(d[i]//2)
s+=f+s[::-1]
print(s)