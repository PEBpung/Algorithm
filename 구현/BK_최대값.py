'''
https://www.acmicpc.net/problem/2562

한줄로 끝낼 수 있는 코드
print(max((int(input()), i+1)for i in range(9)))
'''
max_N = 0
max_I = 0

for i in range(1, 10):
    num = int(input())
    if num > max_N:
        max_N = num
        max_I = i

print(max_N)
print(max_I)


