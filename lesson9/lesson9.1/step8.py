cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
gen = (cities[i % len(cities)] for i in range(1_000_000))
for i in range(20):
    print(next(gen), end=' ')
