'''
https://leetcode.com/problems/trapping-rain-water/

input 
0 1 0 2 1 0 1 3 2 1 2 1
4 2 0 3 2 5         9
'''
from pprint import pprint

def solution(height):
    board = []
    answer = 0
    old_f = 0
    # 보드 생성 
    for i in range(max(height)):
        board.append([1 if i < height[j] else 0 for j in range(len(height))])

    for i, row in enumerate(board):
        flag = False
        score = 0
        for j, v in enumerate(row):
            if flag and v == 1 and old_f == 1:
                old_f = v
                flag = not flag
            elif not flag and v == 1:
                old_f = v
                flag = not flag
                print(flag)
            elif flag and v == 0:
                old_v = 0
                board[i][j] = 3
                score += 1
        if old_f == 1:
            answer += score
    pprint(board)
    return answer

height = list(map(int, input().split()))
print(solution(height))