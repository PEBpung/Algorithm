'''
https://programmers.co.kr/learn/courses/30/lessons/68644
'''
from itertools import combinations as comb

def solution(numbers):
    '''
    Time Complexity: O(n!)
    nCr = n! / (n-r)!r!
    '''
    com = list(map(lambda x: sum(x), comb(numbers, 2)))
    return sorted(list(set(com)))

    