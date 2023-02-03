rub = 1000
n = int(input())
i = 0
while i < n:
    rub *= 1.05
    i += 1
print(round(rub,2))