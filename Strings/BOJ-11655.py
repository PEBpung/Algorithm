'''
https://www.acmicpc.net/problem/11655
'''

s = str(input())
res = str()
for i in s:
    if i.isupper():
        if ord(i) + 13 > ord('Z'):   
            res += chr(((ord(i) + 13) % ord('Z')) + ord('A')-1)
        else:
            res += chr(ord(i) + 13)
    elif i.islower():
        if ord(i) + 13 > ord('z'): 
            res += chr(((ord(i) + 13) % ord('z')) + ord('a')-1)
        else:
            res += chr(ord(i) + 13)
    else:
        res += i

print(res)