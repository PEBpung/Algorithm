'''
https://www.acmicpc.net/problem/10610

마르코는 왜 30을 존경할까.
그리디 문제라고 너무 모든 경우를 포함하려고함 -> 메모리 초과
안되는 경우를 제외하면서 진행하는 방법 체택 
'''
n = input()
# 오름차순으로 입력을 분리해서 정렬
n = sorted(n, reverse=True)
sum = 0

# 10의 배수가 아니면 -1
if '0' not in list(n):
     print('-1')
else:
    for i in n:
        sum += int(i)
    # 3의 배수가 아니면 -1
    if sum % 3 != 0:
        print('-1')
    else:
        print(''.join(n))