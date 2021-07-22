'''
https://programmers.co.kr/learn/courses/30/lessons/12918
'''
def solution(s):
    try:
        list(map(int, s))
        if not len(s) == 4 or len(s) == 6:
            raise
    except:
        return False
    return True