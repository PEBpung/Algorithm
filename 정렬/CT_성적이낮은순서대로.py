'''
학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생 이름을 출력하시오.
3
홍길동 95
이순신 77
강감찬 88
'''

n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda x: x[1])

for s in array:
    print(s[0])