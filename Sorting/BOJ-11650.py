'''
https://www.acmicpc.net/problem/11650
'''
import sys
input = sys.stdin.readline
n = int(input())
input_data = []

for _ in range(n):
    x, y = map(int, input().split())
    input_data.append((x, y))

input_data = sorted(input_data, key=lambda x: (x[0], x[1]))

for i in input_data:
    x, y = i
    print(x, y)