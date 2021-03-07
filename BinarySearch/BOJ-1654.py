'''
https://www.acmicpc.net/problem/1654
2110과 매우 유사한 문제. 
count 설정이 핵심
'''

k, n = map(int, input().split())
array = []
for i in range(k):
    array.append(int(input()))

start = 0
end = max(array)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(k):
        count += array[i] // max(1, mid)

    if n <= count:
        result = mid 
        start = mid + 1 
    else: 
        end = mid - 1 

print(result)