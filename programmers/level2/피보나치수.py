'''
https://programmers.co.kr/learn/courses/30/lessons/12945
'''

def solution(n):
    '''
    time complexity = O(n)
    '''
    dp = [0] * 100001
    dp[1], dp[2] = 1, 1

    for i in range(2, n):
        dp[i+1] = dp[i] + dp[i-1]
    return dp[n] % 1234567

# 2
print(solution(3))