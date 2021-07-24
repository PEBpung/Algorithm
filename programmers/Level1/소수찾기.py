'''
https://programmers.co.kr/learn/courses/30/lessons/12921
'''

# solution1: 모든 수에 대한 for문 이용
# 시간 초과
def solution(num):
    '''
    Time Complexity: O(N^2)
    '''
    answer = [False, False, True]
    for n in range(3, num + 1):
        flag = True
        for i in range(2, n):
            if n % i == 0:
                flag = False
                break
        answer.append(flag)  
    return sum(answer)

# solution2: div 범위 축소, space 축소
# 효율성 통과 (3320.96ms, 11MB)
def solution(num):
    '''
    Time Complexity: O(N√N)
    '''
    answer = [False, False, True]
    for n in range(3, num + 1):
        flag = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                flag = False
                break
        if flag:
            answer.append(flag)  
    return sum(answer)

# solution3: 에라토스테네스의 체
# 효율성 통과 (107.53ms, 24.2MB)
def solution(num):
    '''
    Time Complexity: O(Nlog(log(N))
    Space Complexity: O(N)
    https://doocong.com/algorithm/sieve-of-eratosthenes/
    '''
    prime_list = [False] * 2 + [True] * (num - 1)

    for n in range(2, int(num ** 0.5) + 1):
        if prime_list[n] == True:
            for p in range(2 * n, num + 1, n):
                prime_list[p] = False
    return sum(prime_list)