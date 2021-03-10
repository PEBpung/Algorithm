'''
https://www.acmicpc.net/problem/11724
'''
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    union_parent(parent, a, b)

result = {}
for i in range(1, n +1):
    r = find_parent(parent, i)
    if r not in result.keys():
        result[r] = 1
print(len(result.keys()))

# =========
# 다른 풀이
# =========

'''
.
.

visited = [False] * (n + 1)
res = 0
# 모든 노드를 방문.
for i in range(1, n+1):
    if not visited[i]:
        visited[i] = True
        q = deque()
        q.append(i)

        while q:
            cur = q.popleft()
            # 방문한 노드의 연결된 노드들 방문.
            for j in g[cur]:
                if not visited[j]:
                    q.append(j)
                    visited[j] = True

        res += 1

print(res)
'''