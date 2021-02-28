'''
https://www.acmicpc.net/problem/1699

python으로 하면 시간 초과, pypy3로 해야 통과된다.
'''
import math
n = int(input())
array = []
# 1부터 제곱 수 할당.
for i in range(1, int(math.sqrt(n)) + 1):
    array.append(i**2)

INF = 100002
d = [INF]*100001
d[0] = 0
d[1] = 1
# 제곱수가 들어있는 리스트만큼 반복 시킴
for i in range(len(array)):
    # 만약 더 적은 수로 나타낼 수 있으면 갱신
    for j in range(array[i], n + 1):
        d[j] = min(d[j], d[j - array[i]] + 1)
print(d[n])