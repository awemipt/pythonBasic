import sys

# считывание списка из входного потока (переменную lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
ranks = ['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант', 'капитан', 'майор', 'подполковник', 'полковник']
d = dict(zip(ranks, range(9)))
lst = [row.split('=')for row in lst_in]
lst.sort(key=lambda x: d[x[1]])
