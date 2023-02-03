i = 0
names = input().split()
while i < len(names):
    names[i] = names[i].lower()
    if names[i][0] == names[i][-1]:
        print('ДА')
        break
    i += 1
else:
    print("НЕТ")