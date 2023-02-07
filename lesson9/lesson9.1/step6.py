n = int(input())

gen1 = (abs(x) for x in range(-n, n+1))
gen2 = (x**3 for x in gen1)
for i in range(4):
    print(next(gen2), end= ' ')