'''
5 8 3
2 4 5 4 6
'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
sum_max = 0

# 구현 부분
for i in range(1, m+1):
    if i % k == 0:
        sum_max += data[n-2]
    else:
        sum_max += data[n-1]

print(sum_max)


'''
구현 부분을 수열을 사용하면 더 깔끔한 풀이가 될 수 있다.
count = int(m / (k+1)) * k
count += m % (k+1)

'''
