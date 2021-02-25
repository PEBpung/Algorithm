'''
최대 K번 바꿔치기 연산을 수행하여 A 배열의 합이 최대가 되게 하라.
5 3
1 2 5 4 3
5 5 6 6 5

결과
26
'''

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때 탈출
        break

print(sum(A))

