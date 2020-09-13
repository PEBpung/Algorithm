import heapq as hq
import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
a = [int(input()) for i in range(n)]

h = []

for i in a:
    if i == 0:
        if h:
            ab, c = hq.heappop(h)
            print(c)
        else:
            print(0)
    else:
        hq.heappush(h, (abs(i), i))
