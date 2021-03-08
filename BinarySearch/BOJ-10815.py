'''
https://www.acmicpc.net/problem/10815
'''
def binary_search(t, array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if t == array[mid]:
            return 1
        elif t >= array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
array = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))
array = sorted(array)

for t in target:
    res = binary_search(t, array, 0, n-1)
    print(res, end=' ')