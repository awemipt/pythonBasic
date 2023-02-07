import sys

# считывание списка из входного потока (не меняйте переменную lst_in в программе)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
lst_in = lst_in[1:]
table = tuple((int(order),name,int(mark),passed) for order, name, mark, passed in (tuple(row.split(';')) for row in lst_in))
print(table)
t_sorted = ()
for row in table:
    t_sorted += sorted(row, key=lambda x: (x[1],x[3], x[2],x[0]))
    
mask = [1,3,2,0]

