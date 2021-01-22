'''
https://programmers.co.kr/learn/courses/30/lessons/12977
itertools를 못써서 당황, combination을 직접 구현
'''
def isPrime(a):
    if(a<2):
        return False
    for i in range(2, a):
        if a%i==0:
            return False
    return True

def solution(nums):
    answer = -1
    cnt = 0    
    for i, f in enumerate(nums[:-2]):
        for j, s in enumerate(nums[i+1:-1]):
            for t in nums[i+j+2:]:
                cnt += isPrime(f+s+t)
    answer = cnt
    return answer