'''
수열을 내림차순으로 정렬하는 프로그램을 만드시오.
3
15
27
12
'''
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

print(array)