import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {}
for data in lst_in:
    if data not in d:
        d[data] = 1
        print(f"HTML-страница для адреса {data}")
    else:
        print(f"Взято из кэша: HTML-страница для адреса {data}")