import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
for i, line in enumerate(lst_in):
    while line.count("  "):
        line = line.replace("  ", " ")
        # print(1)
    lst_in[i] = line.replace(" ", "-")
for line in lst_in:
    print(line)