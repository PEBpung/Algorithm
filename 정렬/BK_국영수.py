'''
https://www.acmicpc.net/problem/10825

예제 입력 1 
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

예제 출력 1 
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
import sys

input = sys.stdin.readline

n = int(input())
student = {}

for _ in range(n):
    s = input().split()
    student[s[0]] = []
    student[s[0]].extend(list(map(int, s[1:])))

print(student.items())
def sort_student():
    for i, k in enumerate(student.items()):
        if student[i][1][0] < k[1][0]:
            student[i], k = k, student[i]
        elif student[i][1][0] == k[1][0]:

            if student[i][1][1] > k[1][1]:
                student[i], k = k, student[i]
            elif student[i][1][1] == k[1][1]:

                if student[i][1][2] > k[1][2]:
                    student[i], k = k, student[i]
                elif student[i][1][2] == k[1][2]:

                    if student[i][0] > k[0]:
                        student[i], k = k, student[i]


sort_student()

print(student)


