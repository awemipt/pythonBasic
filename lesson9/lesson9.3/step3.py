import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
# переменную lst_in не менять!
lst2D = [map(int, lst.split()) for lst in lst_in]
for row in lst2D:
    print(*row)