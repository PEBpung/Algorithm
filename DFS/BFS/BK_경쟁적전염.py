'''
https://www.acmicpc.net/problem/18405

런타임 오류가 계속 나서 확인 했더니 NxK가 아니라 NxN이었다. 
다음에는 문제를 잘 확인해야될듯.
deque를 이용하면 좀 더 깔끔한 풀이가 된다.
'''
from collections import deque 

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
sec, end_x, end_y = map(int, input().split())
q = []

dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

for x in range(n):
    for y in range(n):
        if board[x][y] != 0:
            q.append([board[x][y], x, y, 0])

q.sort()
q = deque(q)

while q:
    virus, x, y, time = q.popleft()
    if time == sec:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx >= 0 and nx < n) and (ny >= 0 and ny < n):
            if (board[nx][ny] == 0):
                board[nx][ny] = virus
                q.append((virus, nx, ny, time+1))

print(board[end_x-1][end_y-1])
