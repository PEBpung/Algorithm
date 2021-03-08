'''
https://www.acmicpc.net/problem/10809
'''
s = str(input())
l = [-1] * 26
for i in s:
    l[ord(i) - ord('a')] = s.index(i)
for i in l:
    print(i, end = ' ')