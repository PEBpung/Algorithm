def solution(citations):
    answer = 0
    # 인용 횟수를 내림차순으로 정렬한다.
    citations.sort(reverse=True)
    
    for i, cit in enumerate(citations):
        if cit > i:
            answer = i+1
            continue
        else: break
            
        
    return answer