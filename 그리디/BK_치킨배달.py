'''
https://www.acmicpc.net/problem/15686
'''
from itertools import combinations 

n, m = map(int, input().split())
house, chicken = [], []

for k in range(n):
    input_data = list(map(int, input().split()))
    for i, v in enumerate(input_data):
        if v == 1:
            house.append((k, i))
        elif v == 2:
            chicken.append((k, i))

candidates = list(combinations(chicken, m))

def get_sum(candidate):
    result = 0
    for x, y in house:
        dist = int(1e9)
        for cx, cy in candidate:
            dist = min(dist, abs(x - cx) + abs(y - cy))
        result += dist
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)

