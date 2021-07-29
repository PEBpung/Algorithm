# 3, 30, 34가 있을 때, 34, 3, 30 순으로 정렬해야됨.
# 33 3030 3434 

def solution(numbers):
    numbers = list(map(str, numbers))
    s = sorted(numbers, reverse=True, key = lambda x: x * 3)
    answer = ''.join(s)
    return answer if int(answer) else '0'