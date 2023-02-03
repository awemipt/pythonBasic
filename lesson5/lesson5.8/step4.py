cities = input().split()
cities = [city for city in cities if len(city) > 5]
print(*cities)