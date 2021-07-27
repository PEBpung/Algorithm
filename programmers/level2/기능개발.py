'''
https://programmers.co.kr/learn/courses/30/lessons/42586#

93, 30, 55 /  1, 30, 5
95, 90, 99, 99, 80, 99	/ 1, 1, 1, 1, 1, 1
올림을 해줘야 한다,,, 
'''


import math

def solution(progresses, speeds):
    idx, time = [], []
    o_i = 0

    for p, s in zip(progresses, speeds):
        time.append(math.ceil((100 - p) / s))

    for i in range(len(time)):
        if time[o_i] < time[i]:
            idx.append((o_i, i))
            o_i = i
    idx.append((o_i, len(time)))
    return [y - x for x, y in idx]

progresses = list(map(int, input().split(', ')))
speeds = list(map(int, input().split(', ')))
print(solution(progresses, speeds))