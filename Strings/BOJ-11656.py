'''
https://www.acmicpc.net/problem/11656
'''
s = input()
array = []
temp = ''
for i in range(len(s)-1, -1, -1):
    temp = s[i] + temp
    array.append(temp)

array.sort()
for i in array:
    print(i)