p = [0] * 10
n = 0
while n!=5:
    i = int(input())
    if p[i] == 0:
        p[i] = 1
        n += 1
    else:
        continue
print(*p)