'''
https://programmers.co.kr/learn/courses/30/lessons/42860

sudo 코드
1. A와 Z 방향 중 최소 개수를 구함
    ex> JEROEN -> 9,4,9,12,4,13
2. 왼쪽으로 진행하는 게 빠른지 오른쪽으로 진행하는 게 빠른지 check
3. 빠른 방향으로 이동을 하고 answer에 간 만큼 더함
'''

def solution(name):
    list = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]
    answer = 0
    idx = 0
    while 1:
        answer += list[idx]
        list[idx] = 0
        if sum(list) == 0: 
            break
        left, right = 1, 1
        while list[idx + right] == 0:
            right += 1
        while list[idx - left] == 0:
            left += 1
        if left >= right:
            idx += right
            answer += right
        else:
            idx -= left
            answer += left
    return answer

# 56
print(solution("JEROEN"))