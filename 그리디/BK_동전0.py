'''
https://www.acmicpc.net/problem/11047
예제에 없는 case를 고려하지 못함
여러줄 입력 받는 방법 [int(input()) for _ in range(n)]
'''

n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]
count = 0

for j in range(1, len(A)+1):
    if k >= A[-j]:
        # 사용 가능한 금액 만큼 count
        count += (k // A[-j])
        k %= A[-j]

print(count)