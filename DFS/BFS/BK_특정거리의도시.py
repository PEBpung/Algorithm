'''
https://www.acmicpc.net/problem/18352

어려운 문제를 풀었더니 금방 푼것 같다. 
근데 입력을 input()으로 하니까 시간초과,, 
sys.stdin.readline을 사용하는 것이 그냥 input()보다 4배 빠르다. 
앞으로는 sys.stdin.readline을 쓰는 걸로,,
'''
from collections import deque
import sys

input = sys.stdin.readline

# input 부분.
n, m, k, x = map(int, input().split())
path = [[] for _ in range(n+1)]
visit = [False]*(n+1)
visit[x] = True

# 모든 도시들의 그래프를 만듬.
for _ in range(m):
    start, end = map(int, input().split())
    path[start].append(end)

q = deque()
q.append((x, 0))
ans = []

while q:
    node, cnt = q.popleft()
    # 거리가 조건에 맞으면 추가.
    if cnt == k:
        ans.append(node)
    # 노드와 이어진 경우 확인.
    for gone in path[node]:
        # 방문 한 경우 확인.
        if visit[gone] == True:
            continue
        visit[gone] = True
        q.append((gone, cnt+1))

if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)
