#Напишите программу, которая вводит трёхзначное число и разбивает его на цифры. Например, при вводе числа 123 программа должна вывести «1 2 3».
a=int(input())
c3=a//100
c2=(a%100)//10
c1=a%10
print(c3,c2,c1)

