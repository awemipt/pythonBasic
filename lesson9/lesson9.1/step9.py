f = lambda x: .5 * x ** 2 - 2
a, b = map(int, input().split())
gen = (round(f(x*0.01),2) for x  in range(a*100, 100*(b+1)))
for i in range(20):
    print(next(gen))