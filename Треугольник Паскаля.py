'''Даны два числа n и m. Создайте двумерный массив [n][m] и заполните его по следующим правилам:
Числа, стоящие в строке 0 или в столбце 0 равны 1 (A[0][j]=1, A[i][0]=1). Для всех остальных элементов массива A[i][j]=A[i-1][j]+A[i][j-1],
то есть каждый элемент равен сумме двух элементов, стоящих слева и сверху от него.
Входные данные
Программа получает на вход два числа n и m.

Выходные данные
Выведите данный массив.'''
n,m=map(int,input().split())
a=[]
for i in range(n):
      a.append([0]*m)

for i in range(n):
      for j in range(m):
            if i==0 or j==0:
                  a[i][j]=1
            else:
                  a[i][j]=a[i-1][j]+a[i][j-1]



for i in range(n):
      print(*a[i])