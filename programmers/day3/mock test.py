answer = {1:0, 2:0, 3:0, 4:0, 5:0}

print(max(answer.values()))

answer[1]+= 10

print(answer)

for i, stack in enumerate(answer):
    print(i, stack)
