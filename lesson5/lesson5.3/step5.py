lst = map(int, input().split())
s = 0
for x in lst:
    if x % 2 == 1:
        s += x

print(s)