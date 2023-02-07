def primes():
    n = 2
    yield 2
    while True:
        n += 1
        for i in range(2, int(n**.5)+1):
            if n % i ==0:
                break
        else:
            yield n

gen = primes()
for i in range(20):
    print(next(gen), end=' ')