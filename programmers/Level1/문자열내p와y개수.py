'''
https://programmers.co.kr/learn/courses/30/lessons/12916
'''
from collections import Counter

def solution(s):
    s = s.lower()
    c = Counter(s)
    return c['y'] == c['p']