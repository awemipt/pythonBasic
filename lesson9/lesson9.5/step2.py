import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
lst_in = [[int(x) for x in nums.split()] for nums in lst_in]
z = zip(*zip(*lst_in))
for x in z:
    print(*x, sep=' ')