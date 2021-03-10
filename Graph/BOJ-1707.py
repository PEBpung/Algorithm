'''
https://www.acmicpc.net/problem/1707
'''
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
res = []
for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    colors = [''] * (v + 1)
    color = ['R', 'G']
    colorIdx = False
    isBipart = True

    for i in range(1, v +1):
        if colors[i] == '':
            colors[i] = color[not colorIdx]
            q = deque()
            q.append(i)

            while q:
                cur = q.popleft()
                cidx = color.index(colors[cur])

                for j in graph[cur]:
                    if colors[j] == '':
                        colors[j] = color[not cidx]
                        q.append(j)
                    else:
                        if i != j and colors[j] != color[not cidx]:
                            isBipart = False
                            break

                if not isBipart:
                    break

        if not isBipart:
            break

    print(['YES', 'NO'][not isBipart])

        