number = list(input())

shape = "+7(xxx)xxx-xx-xx"
for i, num in enumerate(number):
    if shape[i] == "x":
        if not num.isdigit():
            print("НЕТ")
            break
    elif shape[i] != num:
        print("НЕТ")
        break
else:
    print("ДА" if len(number)==len(shape) else "НЕТ")