N = int(input())
eye= [[1 if i==j else 0 for j in range(N)]for i in range(N)]
for i in eye:
    print(*i)