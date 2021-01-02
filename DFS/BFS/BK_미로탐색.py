'''
https://www.acmicpc.net/problem/2178

처음에 재귀함수를 사용한 DFS로 풀었더니 시간초과 문제가 생김.
재귀함수 말고 stack으로 풀었는데 답이 계속 틀림.
아무래도 이 문제는 BFS로 풀리는 문제였던 것 같다. 
아래는 queue를 이용한 BFS 코드이다.  
'''

def BFS(board, x, y):
    ''' BFS 를 이용하여 미로 찾기 알고리즘을 구현. 
    :param board: 미로 그래프 
    :param x: 노드의 x 방향 
    :param y: 노드의 y 방향
    :return: 최소 이동 거리 
    '''
    visit = {(x, y), } # 방문한 노드 저장
    queue = [(x, y, 1)] # 노드 x, 노드 y, 이동 거리

    while queue:
        x, y, distance = queue.pop(0)

        n_distance = distance + 1
        # 상하좌우로 이동 가능한 노드를 살핌.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # board의 범위에서 벗어나는 지 검사
            if (nx >= 0 and nx < m) and (ny >= 0 and ny < n):
                # 이동 가능한 칸이고 방문한 적 없는 칸인 경우.
                if (board[ny][nx] == '1') and (((nx, ny) not in visit)):
                    # 도착 지점에 도착한 경우 총 이동 경로를 출력 (BFS이므로 최소가 됨.)
                    if (nx == m-1) and (ny == n-1):
                        return print(n_distance)
                    
                    visit.add((nx, ny)) # 방문
                    queue.append((nx, ny, n_distance)) # 새로운 칸의 좌표와 이동거리 저장.

if __name__ == '__main__':
    n, m = map(int, input().split())

    board = [list(input()) for _ in range(n)]
    # 상하좌우 벡터
    dx, dy= [0, 0, -1, 1], [-1, 1, 0, 0]

    BFS(board, 0, 0)
'''
# DFS로 풀었을 때, 코드.

def DFS(x, y, count):
    stack = [(x, y, 1)]
    visit = {(x, y), }

    while stack:
        x, y, distance = stack.pop()

        n_distance = distance + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx >= 0 and nx < m) and (ny >= 0 and ny < n):
                if (board[ny][nx] == '1') and (((nx, ny) not in visit)):

                    if (nx == m-1) and (ny == n-1):
                        count.append(n_distance)
                        continue
                    
                    visit.add((nx, ny)) 
                    stack.append((nx, ny, n_distance))
    return count

if __name__ == '__main__':
    n, m = map(int, input().split())

    board = [list(input()) for _ in range(n)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    count = []

    count = DFS(0,0, count)
    print(min(count))
'''