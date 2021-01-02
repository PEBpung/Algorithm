'''
https://www.acmicpc.net/problem/14502

무조건 시간초과가 뜰거라고 생각했는데 통과한 문제.
총 세개의 파트로 나뉘어짐.
1. 3개의 벽을 세운다.
2. 바이러스를 뿌려준다.
3. 안전영역을 카운트해준다.
'''
import sys
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]


# 바이러스를 퍼트리는 함수
def spread(board, visit, virus):
    while virus:
        x, y = virus.popleft()
        for dx, dy in (-1,0),(0,-1),(1,0),(0,1):
            nx, ny = x+dx, y+dy
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if board[nx][ny] != 0 or visit[nx][ny]:
                continue
            board[nx][ny] = 2
            virus.append((nx,ny))
            visit[nx][ny] = True
    return board

# 안전 영역과 바이러스 영역 추출
def classifier():
    virus = deque()
    space = []
    for i in range(n):
        for k in range(m):
            if board[i][k] == 0:
                space.append((i,k))
            elif board[i][k] == 2:   
                virus.append((i, k))
                visit[i][k] = True
    return virus, space

# 안전 영역을 세주는 함수.
def count(new_board):
    cnt = 0
    for i in range(n):
        for k in range(m):
            if new_board[i][k] == 0:
                cnt += 1
    return cnt

# 벽을 생성하고 바이러스를 퍼트림.
def make_wall():
    ans = []
    virus, space = classifier()
    # 조합을 이용해서 벽 3개의 좌표를 구함.
    new_wall = combinations(space, 3)
    for wall in new_wall:
        # 다양한 경우를 실험해야 되기때문에 깊은 복사 사용.
        new_board = copy.deepcopy(board)
        new_visit = copy.deepcopy(visit)
        new_virus = copy.deepcopy(virus)
        # 벽을 세움.
        for w in wall:
            x, y = w
            new_board[x][y] = 1
        # 바이러스를 뿌려줌.
        new_board = spread(new_board, new_visit, new_virus)
        # 안전 영역을 카운트해줌.
        ans.append(count(new_board))
    print(max(ans)) 

make_wall()