'''
https://programmers.co.kr/learn/courses/30/lessons/42885
'''

def solution(people, limit):
    answer = 0
    people.sort()
    start, end = 0, len(people) - 1

    while end - start >= 1:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        answer += 1

    return answer + (end == start)

result = solution([70, 50, 80, 50], 100)
print(result)