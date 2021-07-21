'''
https://www.acmicpc.net/problem/10820

이 문제의 경우 반복횟수 N을 입력받는 부분은 없다.
이런 유형의 문제에서는 종료 조건(EOF)이 들어올 때까지 계속해서 입력을 받을 수 있게 구현해야 된다!
그래서 try except문을 활용
'''
def Implement(sentence):
    ans =[0, 0, 0, 0]

    for s in sentence:
        if s.islower():
            ans[0] += 1
        elif s.isupper():
            ans[1] += 1
        elif s.isdigit():
            ans[2] += 1
        elif s == ' ':
            ans[3] += 1

    return ' '.join(map(str, ans))

while True:
    try:
        sentence = input()
        print(Implement(sentence))     
    except EOFError:
        break


