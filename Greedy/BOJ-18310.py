'''
https://www.acmicpc.net/problem/18310
'''
import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))

array.sort()
print(array[(n-1)//2])


