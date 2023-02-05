import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d= {}
for data in lst_in:
    date, name = data.split()
    d.setdefault(date, [])
    d[date].append(name)
for date in d:
    print(f"{date}: ",", ".join(d[date]))