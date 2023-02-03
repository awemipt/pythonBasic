numbers = input().split()
d = {}
for number in numbers:
    if number[:2] not in d:
        d[number[:2]] =[]
    d[number[:2]] += [number]
print(*sorted(d.items()))