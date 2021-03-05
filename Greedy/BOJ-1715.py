'''
https://www.acmicpc.net/problem/1715
'''
import heapq
import sys
input = sys.stdin.readline
n = int(input())
input_data = []
d = [0]*100000
for _ in range(n):
    input_data.append(int(input()))

result = 0
heapq.heapify(input_data)
while len(input_data) > 1:
    a = heapq.heappop(input_data)
    b = heapq.heappop(input_data)
    heapq.heappush(input_data, a+b)
    result += (a + b)
print(result)