a, b, c, d = map(int, input().split())
if a-c>= 2 and b-d>= 2 or a-d>=2 and b-c >= 2:
    print("ДА")
else:
    print("НЕТ")