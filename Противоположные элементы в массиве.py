'''Дан список чисел. Определите, есть ли в нем два противоположных(то есть дающих в сумме 0) числа. Если такие числа есть в массиве,
выведите их индексы в порядке возрастания. Если таких чисел в массиве нет, ничего не выводите. Гарантируется, что таких пар не больше одной.'''
a=list(map(int,input().split()))
n=len(a)
for i in range(n-1):
      for j in range(i+1,n):
            if a[i]+a[j]==0:
                  print(i,j)