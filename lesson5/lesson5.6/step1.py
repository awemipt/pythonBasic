N = int(input())

ans = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(1)
    ans.append(row)
for i in range(N):
    ans[i][-1] = 5
for i in range(N):
    for j in range(N):
        print(ans[i][j], end =' ')
    print()