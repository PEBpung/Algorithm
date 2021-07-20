from collections import deque

def solution(places):
    answer = []
    q = deque()
    
    visit = [[0] * 5 for _ in len(places)]
    return answer