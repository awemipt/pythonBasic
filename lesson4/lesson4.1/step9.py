digit = list(map(int,list(input())))
if sum(digit[3:])==sum(digit[:3]):
    print("ДА")
else:
    print("НЕТ")
