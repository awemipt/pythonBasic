def isTriangle(a, b, c):
    return a + b > c and a + c > b and b + c >a


x, y, z = map(int, input().split())
print(isTriangle(x, y, z))