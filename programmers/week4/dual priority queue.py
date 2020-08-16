'''
문제 설명
이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

명령어	수신 탑(높이)
I 숫자	큐에 주어진 숫자를 삽입합니다.
D 1	큐에서 최댓값을 삭제합니다.
D -1	큐에서 최솟값을 삭제합니다.
이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후
큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

제한사항
operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
operations의 원소는 큐가 수행할 연산을 나타냅니다.
원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서
최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.
입출력 예
operations	return
[I 16,D 1]	[0,0]
[I 7,I 5,I -5,D -1]	[7,5]
'''
import heapq as hq

def solution(operations):
    answer = []
    h = []
    # for 문으로 명령어 하나씩 받는다
    for s in operations:
        # " "을 기준으로 나눈다.
        op = list(str(s).split())
        # 첫번째(영문)을 받고 어떤 명령인지 판단한다.
        # 만약 I라면?
        print(op[0], op[1])
        if op[0] == 'I':
            # 숫자를 넣는다.
            hq.heappush(h, int(op[1]))
        # 만약 D이고 큐가 비어있지 않으면?
        elif op[0] == 'D' and len(h) > 0:
            # 만약 1이라면?
            if op[1] == '1':
                # 최대값을 삭제한다.
                h.remove(max(h))
            # 만약 -1이라면?
            elif op[1] == '-1':
                # 최솟값을 삭제한다.
                hq.heappop(h)
    # 검사해서 비어있으면?
    if(len(h) == 0):
        # [0,0]을 리턴
        answer = [0, 0]
    # 둘 이상이면?
    else:
        # 최대, 최소만 answer에 넣는다.
        answer.append(max(h))
        answer.append(min(h))
    return answer
operations = ['I 7','I 5','I -5','D -1']
# operations = ["I 16","D 1", "I 8"]
solution(operations)
