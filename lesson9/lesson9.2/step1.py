N = int(input())


def get_sum(N):
    s = 0
    for i in range(1,N+1):
        s += i
        yield s

p = get_sum(N)
print(next(p))