'''
선생님이 이상한 출석을 부른다
랜덤으로 출석부를 보고 번호를 부른다. 
0 ~ 23의 숫자를 받아서 중복값을 표시해라
'''

def solution_origin(a, n):  
    d = []
    for i in range(24) :  
        d.append(0)        

    for i in range(n) :    
        d[a[i]] += 1

    return d

def solution_get(a, n):
    d = {}
    for i in a:
        tmp = d.get(i, 0)
        d[i] = tmp + 1
    
    result = [d[x] if x in d.keys() else 0 for x in range(24)]
    return result

from collections import Counter

def solution_counter(a, n):
    d = Counter(a)
    # 24가 아니라 n 이었다면 O(n) 시간 복잡도를 가짐
    result = [d[x] if x in d.keys() else 0 for x in range(24)]
    return result

n = int(input())      
a = map(int, input().split())

# d = solution_origin(a, n)
# d = solution_get(a, n)
d = solution_counter(a, n)

for i in range(1, 24) :  
    print(d[i], end=' ')