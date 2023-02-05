import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {}
for data in lst_in:
    number, name = data.split()
    if name not in d:
        d[name] = []
    d[name] += [number]
print(*sorted(d.items()))