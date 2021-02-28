n = int(input())
odd = []

for i in range(n):
    odd.append(2*i+1)

for i in range(1, n*2):
    if (i <= n):
        print(' '*(i-1)+ '*'*odd[-i])
    if (i > n):
        print(' '*(n - i%n-1)+ '*'*odd[i%n])