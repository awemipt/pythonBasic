import sys

# считывание списка из входного потока


lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
d = {int(value): key for key, value in [x.split(":") for x in lst_in]}
[print(d[x], end=' ') for x in sorted(d)[:3]]