'''
https://www.acmicpc.net/problem/1476
'''

e, s, m = map(int, input().split())

year = 1
ye, ys, ym = 1, 1, 1
while not (ye == e and ys == s and ym == m):
    ye += 1
    ys += 1
    ym += 1
    year += 1

    if ye == 16:
        ye = 1
    if ys == 29:
        ys = 1
    if ym == 20:
        ym = 1

print(year)