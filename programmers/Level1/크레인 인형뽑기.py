'''
https://programmers.co.kr/learn/courses/30/lessons/64061
'''
def stack_check(stack, answer):
    if len(stack) > 1:
        if stack[-1] == stack[-2]:
            stack.pop(-1)
            stack.pop(-1)
            answer += 2
    return stack, answer

def solution(board, moves):
    answer = 0
    stack = []
    
    for move in moves:
        for i, v in enumerate(board):
            if v[move - 1] > 0:
                stack.append(v[move - 1])
                v[move - 1] = 0
                stack, answer = stack_check(stack, answer)   
                break
    return answer