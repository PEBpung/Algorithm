temp = input().split()

try:
    a, b, c = map(int, temp)
except:
    print('다시 입력하세요.')
else:
    d = 1
    while d % a != 0 or d % b != 0 or d % c != 0 :
        d += 1
    print(d)