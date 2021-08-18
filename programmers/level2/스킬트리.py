def find_parent(parent, x):
    # x가 루트노드가 아니면, 찾을 때 까지 반복
    if not x in parent.values(): 
        return False
    if parent[x] != x:
        return find_parent(parent, x)

def solution(skill, skill_trees):
    answer = -1
    graph = {}

    for a, b in zip(skill[1::-1], skill[::-1]):
        graph[a] = []
        graph[a].append(b) 
    
    for tree in skill_trees:
        count = 0
        for i, t in enumerate(tree):
            if not find_parent(graph, t):
                count += 1
            elif find_parent(graph, t) in t[i:]:
                break
        if count == len(tree):
            answer += 1
    return answer


result = solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
print(result)
# >> 2