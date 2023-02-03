import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
flag = False
for i in range(len(lst_in)):
    for j in range(i+1, len(lst_in[i])):
        if lst_in[i][j] != lst_in[j][i]:
            flag = True
            break
    if flag:
        print("НЕТ")
        break
else:
    print("ДА")