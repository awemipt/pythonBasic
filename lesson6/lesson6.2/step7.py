things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
n = int(input()) * 1000
things_r = {v:k for k, v in things.items()}
s = 0
for i in reversed(sorted(things_r)):
    if s + i <= n:
        s += i
        print(things_r[i], end=' ')