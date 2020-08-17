'''
문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
입출력 예
n	result
10	4
5	3'''

def solution(n):
    prime = [2, 3]
    arr = []
    for idx, num in enumerate(range(2, n+1)):
        arr.append(num)
        for p in prime:
            if num % p  == 0:
                arr.remove(num)
                break
        prime = prime + arr

    return len(list(set(prime)))

n = 20
solution(n)