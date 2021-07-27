'''
https://programmers.co.kr/learn/courses/30/lessons/42577

119, 97674223, 1195524421	false
'''
from collections import Counter

def solution(phone_book):
    n = len(min(phone_book))
    for i in range(n, 20):
        crop = list(map(lambda x: x[:i], phone_book))
        prefix = Counter(crop)
        if 2 in prefix.values():
            return True
    return False

phone_book = list(input().split(', '))
print(solution(phone_book))