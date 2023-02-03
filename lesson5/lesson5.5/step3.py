s = input()
it = iter(s)
a = next(it)
while a != ' ':
    print(a, end='')
    a = next(it)
