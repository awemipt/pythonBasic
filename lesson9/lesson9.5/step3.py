import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = [[int(num) for num in l.split()] for l in lst_in]

for row in zip(*lst_in):
    print(*row)