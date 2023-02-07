cities = input().split()
f = filter(lambda x: len(x) > 5, cities)
for i in range(3):
    print(next(f), end=' ')