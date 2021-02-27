'''
입력 
6 4
1 4
2 3
2 4
5 6
'''

def find_parent(parent, x):
    # x가 루트노드가 아니면, 찾을 때 까지 반복
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0]*(v+1)

# 부모노드 자기 자신으로 초기화 
for i in range(1, v+1):
    parent[i] = i
    
# Union 연산을 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end= ' ')

print()

print('부모 노드 집합: ', end=' ')
for i in range(1, v + 1):
    print(parent[i], end=' ')


