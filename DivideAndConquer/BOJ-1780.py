'''
https://www.acmicpc.net/problem/1780
'''
import sys
input = sys.stdin.readline

def check_num(paper):
    h = len(paper[0])
    for i in range(h):
        for j in range(h):
            if paper[i][j] != paper[h-1][h-1]:
                return False
    return True

def divide(paper):
    cut_all = []
    div = len(paper) // 3
    for i in range(3):
        temp = []
        for j in range(3):
            cut = [row[div*i: div*i + div] for row in paper[div*j: div*j + div]]
            temp.append(cut)
        cut_all.append(temp)
    return cut_all

n = int(input())
board = []
for i in range(n):
    array = list(map(int, input().split()))
    board.append(array)

q = [board]
result = [0, 0, 0]
while q:
    paper = q.pop()
    c = check_num(paper)
    if c == True:
        result[paper[0][0] + 1] += 1
    else:
        cut_all = divide(paper)
        for cut in cut_all:
            for c in cut:
                q.append(c)

for i in result:
    print(i)