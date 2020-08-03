def solution(a, b):
    answer = ''

    Midx = [1, -1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']

    sum = 0
    for mon in range(0, a-1):
        sum += (30 + Midx[mon])
    sum += b

    idx = sum % 7 - 1

    answer = day[idx]
    return answer
