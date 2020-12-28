'''
https://www.acmicpc.net/problem/18312

직접 쓰면서 풀어서 쉽게 풀었던 문제.
문제를 잘보면 답이 나온다. 
'''                          

n, k = map(str, input().split())
count = 0

for hour in range(int(n)+1):
    for minute in range(60):
        for sec in range(60):
            # 모든 시간을 합쳐줌, 01 02... 형식으로 바꿔주기 위해 zfill 사용
            time = str(hour).zfill(2) + str(minute).zfill(2) + str(sec).zfill(2)
            if k in time:
                count += 1

print(count)
                    