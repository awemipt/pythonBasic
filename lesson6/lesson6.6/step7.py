import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.raeadlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {}
for data in lst_in:
    author, name = data.split(':')
    d.setdefault(author, set())
    d[author].add(name)
