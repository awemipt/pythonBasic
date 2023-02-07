cities = input().split()
ans = []
tmp =[]
for i in range(len(cities)):
    if len(tmp) == 3 :
        ans.append(tmp)
        tmp = []

    tmp.append(cities[i])
print(ans)
zip
for row in ans:
    print(*row)