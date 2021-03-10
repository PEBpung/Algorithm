'''
https://www.acmicpc.net/problem/10451
'''
from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[array[i - 1]].append(i)
    
    visited = [0] * (n + 1)
    res = 0
    for i in range(n + 1):
        if not visited[i]:
            visited[i] = True
            q = deque()
            q.append(i)
            while q:
                cur = q.popleft()
                for j in graph[cur]:
                    if not visited[j]:
                        visited[j] = True
                        q.append(j)
            res += 1

    print(res - 1)
