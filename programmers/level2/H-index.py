'''
https://programmers.co.kr/learn/courses/30/lessons/42747
'''

def solution(citations):
    answer = 0
    # 인용 횟수를 내림차순으로 정렬한다.
    citations.sort(reverse=True)
    
    for i, cit in enumerate(citations):
        if cit > i:
            answer = i + 1
        
    return answer