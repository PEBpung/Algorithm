'''
https://programmers.co.kr/learn/courses/30/lessons/42883
'''

def solution(number, k):
    stack = []
    for n in number:
        while stack and n > stack[-1] and k > 0:
            k -= 1
            stack.pop()
        
        stack.append(n)
        
    if k != 0:
        stack = stack[:-k]
        
    return ''.join(stack)


result = solution("1924", 2)
# "94"
print(result)

result = solution("1231234", 3)
# "3234"
print(result)

'''
# 시간초과로 인해서 실패
from itertools import combinations 

def solution(number, k):
    val = list(map(''.join, combinations(number, len(number) - k)))
    return max(val)
'''