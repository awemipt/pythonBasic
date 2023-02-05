import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# здесь продолжайте программу (используйте список lst_in и menu)
addMenu = {key: value for key,value in[x.split('=') for x in lst_in]}
menu={**menu, **addMenu}
print(menu)