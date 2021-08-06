'''
https://programmers.co.kr/learn/courses/30/lessons/42626

1, 2, 3, 9, 10, 12   7
0 0 0 0 0  7
'''

import heapq

def solution(scoville, K):
    '''
    Time Complexity: O(N)
    '''
    answer = 0
    
    # 받은 리스트를 힙으로 만든다.
    heapq.heapify(scoville)
    mix = 0

    # K이상일 때까지 순회한다.
    while len(scoville) > 1 and scoville[0] < K:
        min_q = heapq.heappop(scoville)
        mix = min_q + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, mix)
        answer += 1
        
    if scoville[0] < K: 
        return -1
        
    return answer

'''
def solution(scoville, K):
    answer = 0
    scoville.sort()
    for _ in scoville:
        a, b, *scoville = scoville
        if a >= K:
            break
        scoville.insert(0, a + b*2)
        answer += 1
    return answer

scoville = list(map(int, input().split(', ')))
K = int(input())
print(solution(scoville, K))
'''



