def isOdd(x):
    return x % 2 == 1


lst = map(int, input().split())
lst = [x for x in lst if isOdd(x)]
print(*lst)