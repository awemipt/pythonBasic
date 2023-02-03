import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
i = 0
while i < len(lst_in):
    if len(lst_in[i].split())==1:
        print(lst_in[i], end=' ')
        i+=1