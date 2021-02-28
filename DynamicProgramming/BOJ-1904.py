'''
https://www.acmicpc.net/problem/1904

피보나치 함수를 사용하면 된다.

잘 생각해보면 00은 길이가 2이기 때문에 i-1번째에서는 붙일 수가 없다. 
따라서 i-2번째에서 00을 붙여 만드는 경우와 i-1번째에서 1을 붙여 만들 수 있는 경우의 합이다.

그런데 여기서 질문을 제기할 수 도 있다. 왜 i-2번째에서 1을 2개 붙여 만드는 경우는 생각하지 않는가?
그 이유는 바로 i-1번째에서 1을 붙여 만드는 경우와 중복되기 때문에다. 

d = [0]*n 하면 런타임 에러(IndexError) ㅠㅠ
'''
import sys
input = sys.stdin.readline
n = int(input())
d = [0]*(1000001)
d[1] = 1
d[2] = 2

for i in range(3,n+1):
    d[i]=(d[i-1]+d[i-2])%15746
print(d[n])   