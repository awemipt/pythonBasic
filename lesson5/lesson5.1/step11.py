n, m = map(int, input().split())
n = n + 1 - n%2
while n < m+1:
    print(n, end = " ")
    n += 2