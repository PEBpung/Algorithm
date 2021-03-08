'''
https://www.acmicpc.net/problem/10808
'''
s = str(input())
l = [0] * 26
for i in s:
    l[ord(i) - ord('a')] += 1
for i in l:
    print(i, end = ' ')