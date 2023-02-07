cities = input().split()
cities = map(lambda x: x if len(x) > 5 else '-', cities)
print(" ".join(cities))