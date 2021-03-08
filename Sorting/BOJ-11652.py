'''
https://www.acmicpc.net/problem/11652
'''
import sys
intput = sys.stdin.readline
n = int(input())
l = {}

for i in range(n):
    v = int(input())
    if v not in l.keys():
        l[v] = 0
    l[v] += 1

mv = max(l.values())

for i in sorted(l.keys()):
    if l[i] == mv:
        print(i)
        break