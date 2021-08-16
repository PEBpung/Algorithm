'''
https://programmers.co.kr/learn/courses/30/lessons/60058
'''

# 문자열 w를 u, v로 분리하는 함수
def get_uv(_u):
    left, right = 0, 0

    for i in range(len(_u)):
        if _u[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return _u[:i+1], _u[i+1:]
    
# 문자열 u가 올바른 괄호 문자열인지 확인하는 함수
def isBalanced(_u):
    stack = []
    for val in _u:
        if val == '(':
            stack.append(val)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    answer = ''

    if not p:
        return answer

    u, v = get_uv(p)
    
    if isBalanced(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'

        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
                
    return answer

result = solution("(()())()")
# "(()())()"
print(result)

result = solution("()))((()")
# "()(())()"
print(result)