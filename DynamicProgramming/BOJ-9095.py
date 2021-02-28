'''
https://www.acmicpc.net/problem/9095
'''
t = int(input())
array = []
d = [0]*12
d[1] = 1
d[2] = 2
d[3] = 4
for _ in range(t):
    array.append(int(input()))

for j in range(t):
    n = array[j]
    for i in range(4, n + 1):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3] 
    print(d[n])