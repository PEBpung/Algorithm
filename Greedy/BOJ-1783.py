'''
https://www.acmicpc.net/problem/1783

생각할게 많았던 문제, 예외처리의 중요성!
차근차근 제외하며 생각하니까 좀 더 깔끔해졌다. 
그리디 문제라고 모든 경우를 고려하면 메모리 초과.
'''

n, m = map(int, input().split())
ans = 1 

if n > 2:
    if m > 6:
         # 2번과 3번의 경우를 모두 사용해야 됨
        ans = m-2 
    else:
        # 6이하인 경우 모든 경우를 사용할 수 없다. 
        # 1번과 4번을 이용하는게 최대값
        ans = min(4, m)
elif n == 2:
    if m > 6:
        # 2가지 경우만 가능해서 4로 고정
        ans = 4
    else: 
        # 출발지까지 포함이므로 +1
        ans = (m+1)//2
print(ans)