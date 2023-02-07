import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)

goods = tuple(map(tuple, (x.split('=') for x in lst_in)))
heavy = filter(lambda x: int(x[1]) > 500, goods)
[print(x[0], end=' ')for x in heavy]