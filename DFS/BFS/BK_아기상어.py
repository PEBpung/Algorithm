'''
https://www.acmicpc.net/problem/16236

처음에는 deque를 사용해서 sort를 했으나, heapq로 변경.
방문여부(visit)을 set로 사용하니까 틀림. [False, True] 로 변경후 통과
BFS를 응용한 문제라서 어려웠던 것 같다. 

https://vipeveloper.tistory.com/162[참고]
'''
from heapq import heappush, heappop

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
q = []

# 상, 하, 좌, 우
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

# 물고기 위치 파악
for i in range(n):
    for k in range(n):
        if board[i][k] == 9:
            heappush(q, (0, i, k))
            board[i][k] = 0

visit = [[False]*n for _ in range(n)]
size, ans, eat = 2, 0, 0

while q:
    time, x, y = heappop(q)
    # (1) 먹기 부분
    if 0 < board[x][y] < size:
        eat += 1
        board[x][y] = 0
        if eat == size:
            size += 1
            eat = 0
        ans += time 
        time = 0
        q.clear()
        visit = [[False]*n for _ in range(n)]

    # (2) 이동 부분 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 보드 안에 있는 지 확인
        if (nx >= 0 and nx < n) and (ny >= 0 and ny < n) :
            # 물고기의 크기 확인, 방문 여부 확인!
            if (board[nx][ny] <= size) and visit[nx][ny]==False:
                heappush(q, (time+1, nx, ny))
                visit[nx][ny]= True
 
print(ans)

