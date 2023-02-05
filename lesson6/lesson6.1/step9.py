d = {}
while (n:=int(input()))!=0:
    if n not in d:
        d[n] = round(n**.5, 2)
        print(d[n])
    else:
        print(f"значение из кэша: {d[n]}")