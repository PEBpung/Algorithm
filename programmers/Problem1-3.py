def solution(n, lost, reserve):
    answer = 0

    student = []

    for num in range(n):
        student.append(1)

    for rm in lost:
        student[rm-1] -= 1

    for ad in reserve:
        student[ad-1] +=1

    for a in range(0, len(student)-1):
        fs = student[a]
        sc = student[a+1]
        if [fs, sc] == [2, 0] or [fs, sc] == [0, 2]:
            student[a], student[a+1] = 1, 1

    for idx in student:
        if idx >= 1:
            answer += 1

    return answer

n, lost, reserve = 5,[2, 4], [3]
solution(n, lost, reserve)
