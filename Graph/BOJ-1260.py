'''
https://www.acmicpc.net/problem/1260
'''
from collections import deque

n, m, v = map(int, input().split())
visit = [0] * (n + 1)
visit[v] = 1
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i] = sorted(graph[i])

def dfs(now, res):
    res.append(now)
    for i in graph[now]:
        if visit[i] == 0:
            visit[i] = 1
            dfs(i, res)

result = []
dfs(v, result)
for i in result:
    print(i, end = ' ')
print()

def bfs(q):
    result = []
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = 1
    for i in result:
        print(i, end = ' ')

visit = [0] * (n + 1)
q = deque([v])
visit[v] = 1
bfs(q)