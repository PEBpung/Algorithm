'''
https://programmers.co.kr/learn/courses/30/lessons/60057
'''
def divide(s, length):
    result, d = '', ''
    p = {}
    k = 0
    
    for i in range(0, len(s), length):
        div = s[i:i+length]
        if d != div:
            result += div
            # 이름을 구분하기 위함
            k += 1
        else:
            name = div + str(k)
            p.setdefault(name, 1)
            p[name] += 1
        d = div
    return len(result) + len(''.join(map(str, p.values())))

def solution(s):
    divider = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2 + 1):
        divider.append(divide(s, i))
    return min(divider)

#result = solution("aaaaaaaaaa")
# 7
#print(result)

result = solution("bbaabaaaab")
# 7
print(result)
