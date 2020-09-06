import heapq as hq

jobs = [[0, 3], [1, 9], [2, 6]]
j = [3, 4, 1, 2, 5]

hq.heapify(jobs)
pq = []

for i in range(len(jobs)):
    point, lenth = hq.heappop(jobs)
    hq.heappush(pq, [point + lenth, point, lenth])

# 처음 에는 그냥 더해준다.
totall = hq.heappop(pq)[0]
time = [totall]

for q in pq:
    t, p, l = q
    if totall > p:
        time.append(totall - p + l )
        totall += l
    elif totall < p:
        totall += t
        time.append(totall - p)

print(totall)
print(time)
