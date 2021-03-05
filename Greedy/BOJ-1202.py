'''
https://www.acmicpc.net/problem/1202
heapq를 추가했더니 시간초과 해결
bag도 sort()를 사용해서 정렬
'''
import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
jual, ruby = [], []
bag = []
result = 0
for _ in range(n):
    m, v = map(int, input().split())
    jual.append((m, v))
for _ in range(k):
    bag.append(int(input()))
jual = sorted(jual, key=lambda x: x[0])
bag.sort()
i = 0 
for b in bag:
    while i < n and b >= jual[i][0]:
        heapq.heappush(ruby, -jual[i][1])
        i += 1
    if ruby:
        result += heapq.heappop(ruby)
print(-result)

# for i in range(k):
#     for j in range(n):
#         if bag[i] < jual[j][0]:
#             continue
#         else:
#             result += jual[j][1]
#             del jual[j]
#             n = n-1
#             break
    