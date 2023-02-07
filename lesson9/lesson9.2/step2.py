N = int(input())


def fib3(N):
    first = 1
    second = 1
    third = 1
    yield first
    yield second
    yield third
    for i in range(N-3):
        first, second, third = second, third, first+ second+ third
        yield third

s = fib3(N)

for i in range(N):
    print(next(s), end=' ')