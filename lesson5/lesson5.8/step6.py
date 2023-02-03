N = int(input())

ans = [[i for j in range(N)] for i in range(N)]
for row in ans:
    print(*row)