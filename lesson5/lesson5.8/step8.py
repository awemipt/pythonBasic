a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [a[i] + b[i] for i in range(len(a))]
print(*c)
