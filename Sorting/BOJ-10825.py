'''
https://www.acmicpc.net/problem/10825

input은 여러 타입으로 받을 수 있음.
sorted 함수는 정렬 순서를 지정해줄 수 있어서 유용. 
'''
import sys
input = sys.stdin.readline

n = int(input())
student = []

# 과목 별로 input 나눔
for _ in range(n):
    name, kor, eng, math = map(str, input().split()) 
    student.append([name, int(kor), int(eng), int(math)])

# sorted 함수를 사용해서 정렬 순서 지정  
student = sorted(student, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in student:
    print(s[0])

'''
입력 
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90

출력
Donghyuk
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
'''