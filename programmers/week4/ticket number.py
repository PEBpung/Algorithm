'''
문제 설명
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.

입출력 예
numbers	         target	  return
[1, 1, 1, 1, 1]	 3	      5
'''
from itertools import combinations as com

def solution(numbers, target):
    answer = 0
    # for문으로 갯수를 입력 받는다. (뺠셈 수)
    for i in range(len(numbers)+1):
        # combination으로 모든 경우의 수를 입력 받는다.
        for c in list(com(numbers, i)):
            # numbers의 sum과 2*선택된 수의 sum을 빼준다.
            diff = sum(numbers) - 2*sum(c)
            # 결과 값이 target과 같으면 answer에 1을 더해준다.
            if diff == target:
                answer += 1
    print(answer)

numbers = [1, 1, 1, 1, 1]
target = 3
solution(numbers, target)
