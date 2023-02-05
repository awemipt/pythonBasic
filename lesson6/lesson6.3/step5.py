cities = input().split()
print(*tuple((city for city in cities if city != 'Ульяновск')))