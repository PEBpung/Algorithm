'''
https://www.acmicpc.net/problem/11728
'''

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = A + B
result = sorted(result)
for i in result:
    print(i, end=' ')
