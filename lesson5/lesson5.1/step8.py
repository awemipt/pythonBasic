a = 1
b = 1
n = int(input())
i = 0
while i < n:
    print(a, end=' ')
    a, b = b, a+b
    i += 1
