def isLarge(s):
    return len(s) >= 6


cities = input().split()

cities = [city for city in cities if isLarge(city)]
print(*cities)