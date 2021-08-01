
# [2, 1, 3, 2]	2

from collections import deque
def solution(priorities, location):
  answer = 0

  value = deque([(v,i) for i,v in enumerate(priorities)])

  while len(value):
      item = value.popleft()
      if max(value)[0] > item[0]:
          value.append(item)
      else:
          answer += 1
          if item[1] == location:
              break
  return answer

priorities = list(map(int, input().split(', ')))
location = int(input())

solution(priorities, location)

