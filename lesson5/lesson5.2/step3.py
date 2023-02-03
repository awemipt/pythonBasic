prod = 1
while True:
    x = int(input())
    if x == 0:
        break
    if x < 0:
        continue
    prod *= x
print(prod)
