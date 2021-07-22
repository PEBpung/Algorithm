'''
https://programmers.co.kr/learn/courses/30/lessons/12910
'''

def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]
    if not answer:
        return [-1]
    return sorted(answer)
    # return arr if len(arr) != 0 else [-1];