'''
https://programmers.co.kr/learn/courses/30/lessons/42577

119, 97674223, 331195524421	false
'''
def solution(phone_book):
    phone_book.sort() 
    for a in range(len(phone_book)-1):
        if phone_book[a] in phone_book[a+1] :
            return False
    return True

# from collections import Counter
# 119, 97674223, 1195524421
# 119 2, 976 1,
# def solution(phone_book):
#     n = len(min(phone_book))
#     for i in range(n, 10):
#         crop = list(map(lambda x: x[:i], phone_book))
#         prefix = Counter(crop)
#         if 2 in prefix.values():
#             return True
#     return False

phone_book = list(input().split(', '))
print(solution(phone_book))
