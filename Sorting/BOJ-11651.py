'''
https://www.acmicpc.net/problem/11651
'''
n = int(input())
array = []
for _ in range(n):
    a, b = map(int, input().split())
    array.append((a, b))

array = sorted(array, key=lambda x: (x[1], x[0]))
for i in array:
    print(i[0], i[1])