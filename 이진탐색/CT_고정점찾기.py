'''
5
-15 -6 1 3 7
'''

n = int(input())
array = list(map(int, input().split()))

array.sort()

for i in range(n):
    if array[i] == i:
        print(array[i])
