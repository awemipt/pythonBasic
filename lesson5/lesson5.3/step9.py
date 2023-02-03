lasts= ['ы','ъ','ь']
cities = input().split()
cities = [x.lower() for x in cities]
first = cities[0][-1]
last = cities[0][0]
for city in cities:
    if city[0] != last:
        print("НЕТ")
        break
    last = city[-1]
    if city[-1] in lasts:
        last = city[-2]

else:
    print("ДА")