a, b = map(int, input().split())
absf = (abs(x) for x in range(a, b+1))
for i in range(5):
    print(next(absf))