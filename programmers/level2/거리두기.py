import sys
input = sys.stdin.readline

def solution(places):
    answer = []
    # place 별로 쪼개기
    for place in places:
        old_answer = len(answer)
        # 입력에서 면접자 위치 가져오기
        P = []
        for x, line in enumerate(place):
            for y, value in enumerate(line):
                if value == "P":
                    P.append((x, y))
        if not P:
            answer.append(1)
            continue
        # 면접자 주위 돌아보기
        semi = 1
        for p in P:
            # 일단 바로 옆에 있으면 바로 fail
            arround = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for dx, dy in arround:
                nx, ny = p[0] + dx, p[1] + dy
                # 면접장의 크기를 초과하면 넘어감
                if nx >= 5 or nx < 0 or ny >= 5 or ny < 0:
                    continue
                if place[nx][ny] == "P":
                    semi = 0
                    break
        if semi == 0:
            answer.append(semi)
            continue 

        # 면접자 주위 돌아보기
        semi = 1
        for p in P:
            # 만약 면접자 주위에 다른 사람이 있으면?
            manhattan = [(0, -2), (0, 2), (-2, 0), (2, 0),
                            (1, -1), (1, 1), (-1, 1), (1, 1)]
            for dx, dy in manhattan:
                nx, ny = p[0] + dx, p[1] + dy
                # 면접장의 크기를 초과하면 넘어감
                if nx >= 5 or nx < 0 or ny >= 5 or ny < 0:
                    continue
                else:
                    # 사람이 존재한다면?
                    if place[nx][ny] == "P":
                        # 그 사람 사이의 장애물 유무 판단.
                        if 2 in (dx, dy) or -2 in (dx, dy):
                            dx, dy = dx // 2, dy // 2
                            cx, cy = p[0] + dx, p[1] + dy
                            if place[cx][cy] == "O":
                                semi = 0
                                break
                        else:
                            cpos = (0, dy), (dx, 0) 
                            for dx, dy in cpos:
                                cx, cy = p[0] + dx, p[1] + dy
                                if place[cx][cy] == "O":
                                    semi = 0
                                    break
        answer.append(semi)
            
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))
'''
places	
[
    [
        "POOOP", 
        "OXXOX", 
        "OPXPX", 
        "OOXOX", 
        "POXXP"
    ], 

    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]	
  
result
[1, 0, 1, 1, 1]

'''
