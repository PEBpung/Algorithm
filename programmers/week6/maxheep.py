'''

문제

수빈이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 수빈이가 정수를 하나씩 외칠때마다 동생은 지금까지 수빈이가 말한 수 중에서 중간값을 말해야 한다. 만약, 그동안 수빈이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 수빈이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 수빈이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.
입력

첫째 줄에는 수빈이가 외치는 정수의 개수 N이 주어진다. N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다. 그 다음 N줄에 걸쳐서 수빈이가 외치는 정수가 차례대로 주어진다. 정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.
출력

한 줄에 하나씩 N줄에 걸쳐 수빈이의 동생이 말해야하는 수를 순서대로 출력한다.


'''
import heapq as hq

def heap_sort(unsorted, sorted) :

    n = len(unsorted)
    hq.heapify(unsorted)

    for idx in range(n) :
        sorted.append(hq.heappop(unsorted))
        hq.heapify(unsorted)
    return sorted


def solution(input):
    mem = []
    # 값을 순서대로 받는다.
    for cnt, number in enumerate(input):
        mem.append(number)
        # 지금까지 나온 수를 정렬한다.
        mem = heap_sort(mem, [])
        # 만약 주어진 수가 짝수라면?
        if (cnt+1)%2 == 0:
            # 중간값 중에 작은 수를 말한다.
            print(min(mem[cnt // 2], mem[cnt//2 +1]))
        else:
            print(mem[cnt//2])

input = [1, 5, 2, 10, -99, 7, 5]

solution(input)
