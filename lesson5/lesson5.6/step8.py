n = int(input())
for i in [2**n for n in range(7)][::-1]:
    while n > i-1:
        n -= i
        print(i, end=" ")