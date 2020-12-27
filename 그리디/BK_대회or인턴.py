'''
https://www.acmicpc.net/problem/2875

min, max를 잘 사용해서 while문을 사용하지 않음.
생각한 것보다 더 깔끔한 코드가 있다.
https://claude-u.tistory.com/402
'''
n, m, k = map(int, input().split())
c_list = []

# 2명의 인원을 무작위로 추출한다.
for i in range(k+1):
    ni = n - i
    mi = m -(k-i)
    count = min(ni//2, mi//1)
    c_list.append(count)

print(max(c_list))
