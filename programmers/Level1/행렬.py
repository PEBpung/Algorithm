'''
https://programmers.co.kr/learn/courses/30/lessons/12950
'''
def solution(arr1, arr2):
    answer = []
    for ar1, ar2 in zip(arr1, arr2):
        ans = []
        for a1, a2 in zip(ar1, ar2):
            ans.append(a1+a2)
        answer.append(ans)
    return answer