a = input().split()
ans = [[a[i], int(a[i + 1])] for i in range(0, len(a), 2)]
print(ans)
