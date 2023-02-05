def minMaxProd(x, y):
    return x * y


lst = list(map(int, input().split()))
print(minMaxProd(min(lst), max(lst)))