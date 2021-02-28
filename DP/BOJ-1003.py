'''
https://www.acmicpc.net/problem/1003

피보나치 함수는 재귀함수를 사용하기 때문에 시간 복잡도가 O ~(fibo(n)) 이 된다
n이 커질 수록 시간복잡도가 증가함으로 dp를 사용해야 된다.
'''
MAX=41
zero, one = [1, 0], [0, 1]

for i in range(2, MAX):
    zero.append(zero[i-1]+zero[i-2])
    one.append(one[i-1]+one[i-2])

t = int(input())
for _ in range(t):
    n = int(input())
    print(zero[n], one[n])
