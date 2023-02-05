def fib_rec(N, f=[]):
    if len(f) == 0:
        f.append(1)
        return fib_rec(N-1, [1])
    elif len(f) == 1 and N >0:
        f.append(1)
        return fib_rec(N-1, [1, 1])
    elif N > 0:
        f.append(f[-1]+f[-2])
        return fib_rec(N-1, f)
    return f

N = int(input())
print(fib_rec(N, []))