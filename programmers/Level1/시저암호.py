'''
https://programmers.co.kr/learn/courses/30/lessons/12926
'''

def Caesar(s, n, a):
    tmp = (ord(s) + n - a) % 26 + a
    return chr(tmp)

def solution(string, n):
    answer = ''
    string = list(string)
    
    for s in string:
        if s.islower():
            answer += Caesar(s, n, ord('a'))
        elif s.isupper():
            answer += Caesar(s, n, ord('A'))
        elif s == ' ':
            answer += ' '
    return answer