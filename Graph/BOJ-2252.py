'''
https://www.acmicpc.net/problem/2252
'''
from collections import deque

v, e = map(int, input().split())
# 진입차수를 0으로 초기화
indegree = [0] * (v + 1)
# 그래프 초기화
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) 
    indegree[b] += 1
    
def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)
    while q:
        a = q.pop()
        result.append(a)
        
        for b in graph[a]:
            indegree[b] -= 1
            if indegree[b] == 0:
                q.append(b)
                
    for i in range(len(result)):
        print(result[i], end = ' ')
 
topology_sort()