'''
https://programmers.co.kr/learn/courses/30/lessons/12939
'''

def solution(s):
    token = list(map(int, s.split(' ')))
    return str(min(token)) + ' ' + str(max(token))

# "1 4"
print(solution("1 2 3 4"))
#"-4 -1"
print(solution("-1 -2 -3 -4"))

