cities = input().split()
i = 0
f = True
while i < len(cities):
    if len(cities[i]) < 5:
        f = False
        break
    i += 1
print("ДА" if f else "НЕТ")
