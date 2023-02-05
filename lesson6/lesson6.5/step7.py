n = int(input())
s = set()
if n % 2 == 0:
    s.add(2)

if n % 3 == 0:
    s.add(3)
if n % 5 == 0:
    s.add(5)
if len(s) == 3:
    print("ДА")
else:
    print("НЕТ")