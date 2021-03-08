'''
https://www.acmicpc.net/problem/10814
'''

n = int(input())
array = []
for _ in range(n):
    a, b = input().split()
    array.append((int(a), str(b)))
array.sort(key=lambda x: x[0])
for i in array:
    print(i[0], i[1])