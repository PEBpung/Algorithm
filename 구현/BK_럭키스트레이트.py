'''
https://www.acmicpc.net/problem/18406

항상 더 깔끔한 코드가 있음에 유념하자.
쉬운 문제는 깔끔하게 고치기.
'''

n = input()
sum =[0, 0]

for i in range(len(n)//2):
    sum[0] += int(n[i])
    sum[1] += int(n[-(i+1)])

if sum[0] == sum[1]:
    print('LUCKY')
else:
    print('READY')
