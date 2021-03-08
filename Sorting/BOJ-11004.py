'''
https://www.acmicpc.net/problem/11004
'''
n, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
print(array[k-1])