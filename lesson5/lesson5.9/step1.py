import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
ans = [lst_in[j][i] for j in range(len(lst_in) - 1, -1, -1) for i in range(len(lst_in[j]) - 1, -1, -1)]
print(*ans)