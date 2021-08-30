'''
https://programmers.co.kr/learn/courses/30/lessons/12973
'''

def solution(s):
    answer = -1
    ord_v = ''
    for i, v in enumerate(s):
        if ord_v == v:
            s = s[:i-1] + s[i+1:]
        ord_v = v
    return answer

#1
print(solution('baabaa'))