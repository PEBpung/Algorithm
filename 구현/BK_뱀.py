'''
https://www.acmicpc.net/problem/3190

정답률 36%도 생각보다 어렵다,,
함수로 쪼개서 문제를 해결하는 방법이 중요한듯
회전 행렬은 답이 안나와서 참고함.
직접 노트에 안적으면 못푸는 문제였던 것 같다.
'''
import math

# 회전 행렬 생성 함수
def R(x):
    return [[round(math.cos(x)), -round((math.sin(x)))],[round(math.sin(x)), round(math.cos(x))]]

# L이면 좌로 회전, D면 우로 회전
def Rotation(order, vector):
    result = []
    if order == 'L': #left
        rMatrix = R(math.radians(90))
    elif order == 'D': #right
        rMatrix = R(math.radians(-90))

    for i in range(len(rMatrix)):
        tmpVal = 0
        for j in range(len(rMatrix[0])):
            tmpVal += rMatrix[i][j] * vector[j]
        result.append(tmpVal)

    return result

# 명령에 맞춰 지렁이 움직임 수행
def implement(point, vector, order):
    point[0] = point[0] + vector[0]
    point[1] = point[1] + vector[1]
    if order != 'G':
        vector = Rotation(order, vector)
    return point, vector

# 동작 메인 부분 
if __name__ == '__main__':
    n = int(input())
    kin = int(input())
    # 게임 보드 생성
    board = [[0]*n for _ in range(n)]

    # 보드에 사과 배치
    for k in range(kin):
        row, col = map(int, input().split())
        board[row-1][col-1] = 1

    info = {}
    lin = int(input())
    # 명령어 저장
    for l in range(lin):
        k, v = map(str, input().split())
        info[int(k)] = v

    point = [0,0]
    vector = [0, 1] 
    tail = []
    sec = 0

    while(True):
        sec += 1
        order = 'G'
        if sec in info.keys():
            order = info[sec]
        tail.insert(0, point.copy())
        point, vector = implement(point, vector, order)

        # 보드에서 이탈하면 정지
        if (0 > point[0] or point[0]>=n) or (0 > point[1] or point[1]>=n):
            break
        # 지렁이 몸통에 부딪히면 정지
        elif point in tail:
            break
        else:
            # 사과가 없다면 꼬리를 없앰
            if board[point[0]][point[1]] == 0:
                tail.pop()
            # 사과가 있으면 먹고 0으로 변경
            else:
                board[point[0]][point[1]] = 0
    print(sec)


'''
6
5 
1 2
1 3
1 4
2 4
2 3
3
3 D
4 D
5 D
'''