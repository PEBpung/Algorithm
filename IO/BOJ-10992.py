'''
https://www.acmicpc.net/problem/10992
'''

n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i), end = '')
    if i == n:
        for j in range(2*i - 1):
            print('*', end = '')
    elif i == 1:
        print('*', end = '')
    else:
        print('*' + ' ' * (2*(i-1)-1) + '*', end = '')
    print()