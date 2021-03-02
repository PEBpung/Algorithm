'''
https://www.acmicpc.net/problem/1302
'''
import sys 
input = sys.stdin.readline

n = int(input())
title = {}

# 책 제목 카운트.
for _ in range(n):
    sell = input().split().pop()
    if sell not in title.keys():
        title[sell] = 0
    title[sell] += 1
# 가장 많이 팔린 책 제목 추출
best_title = [k for k, v in title.items() if v == max(title.values())]
# 정렬 후 맨 앞에 값 출력
best_title.sort()
print(best_title[0])
