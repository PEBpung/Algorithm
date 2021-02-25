'''
https://www.acmicpc.net/problem/5585
'''
n = 1000 - int(input())
count = 0

coin_types = [500, 100, 50, 10, 5, 1]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin 

print(count)

'''
n = int(input())

charge = 1000 - n
coin = [500, 100, 50, 10, 5, 1]

index, count = 0, 0

while charge > 0:
    if charge < coin[index]:
        index += 1
        continue
    else:
        charge -= coin[index]
        count += 1

print(count)
'''