'''
https://www.acmicpc.net/problem/2110
'''

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array = sorted(array)

start = 0
end = max(array)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    cur_pos = array[0]
    #  mid 만큼 떨어질 수 있는 공유기 개수를 구함.
    for i in range(1, n):
        if cur_pos + mid <= array[i]:
            count += 1
            cur_pos = array[i]
    # 만약 공유기가 설치 되는 개수가 많다면 mid (거리)를 증가.
    if count >= m:
        result = mid
        start = mid + 1
    else: 
        end = mid - 1  # the

print(result)


    