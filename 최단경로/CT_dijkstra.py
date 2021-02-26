'''
입력 
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

결과 
0
2
3
1
2
4
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리된 노드이면 건너뛴다. (기존의 거리보다 크니까 이미 더 짧은 경로가 존재함.)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 만약 기존의 거리보다 들어온 경로의 거리가 짧다면 바꿔준다.
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
dijkstra(start)

for i in range(1, n+1):
    # 도달할 수 없는 경우 무한이라고 출력
    if distance[i] == INF:
        print('무한')
    else:
        print(distance[i])