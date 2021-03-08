'''
https://www.acmicpc.net/problem/10989
입력이 너무 많을 때는 계수 정렬 사용.
데이터 개수 N개, 최대값의 크기를 K라고 할 때,
시간 복잡도는 O(N + K)이다.
'''

import sys
input = sys.stdin.readline
m = 10001
l = [0]*m
for _ in range(int(input())) : 
    l[int(input())] += 1
for i in range(1,m):
    print(f"{i}\n" * l[i], end = "")