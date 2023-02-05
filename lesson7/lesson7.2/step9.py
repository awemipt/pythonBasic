def sLen(s):
    return s, len(s)


cities = input().split()
d = {city: Len for city, Len in [sLen(city) for city in cities]}
a = sorted(d, key=lambda x: d[x])
print(*a)
