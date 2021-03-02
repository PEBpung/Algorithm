'''
https://www.acmicpc.net/problem/2751
'''
import sys
input = sys.stdin.readline
n = int(input())
input_data = []
for i in range(n):
    input_data.append(int(input()))

input_data.sort()

for i in input_data:
    print(i)