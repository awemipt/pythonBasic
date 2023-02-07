import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
d = {key: int(value) for key, value in [row.split("=") for row in lst_in]}
print(*sorted(d,reverse=True, key=lambda x: d[x]))
