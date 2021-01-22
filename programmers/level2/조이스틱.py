'''
https://programmers.co.kr/learn/courses/30/lessons/42860#
테스트 케이스 11 때문에 틀렸던 문제.
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