'''
https://programmers.co.kr/learn/courses/30/lessons/42862

입출력 예
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
'''
import sys
input = sys.stdin.readline

def solution(n, lost, reserve):
    answer = 0
    student = [0 if x + 1 in lost else 1 for x in range(n)]

    for i in reserve:
        student[i - 1] += 1
    
    for j in range(n - 1):
        if sum(student[j:j+2]) == 2 and min(student[j:j+2]) == 0:
            student[j], student[j+1] = 1, 1
    return sum(map(lambda x: x > 0, student))

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))

print(solution(n, lost, reserve))
