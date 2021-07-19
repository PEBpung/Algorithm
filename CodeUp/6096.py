from pprint import pprint

def solution_bin(board, row, col):
    wise = [1, 0]
    for idx, r in enumerate(board):
        r[col - 1] = wise[r[col - 1]]
        if idx == row - 1:
            r[:] = [wise[r[i]] for i in range(len(r))]
    pprint(board)
    

board = []
for i in range(19):
    board.append(list(map(int, input().split())))
n = int(input())

for _ in range(n):
    row, col = list(map(int, input().split()))
    solution_bin(board, row, col)