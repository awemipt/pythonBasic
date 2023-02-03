import math

n= int(input())
for i in range(2, math.ceil(n**.5)+1):
    if n%i ==0:
        print("НЕТ")
        break
else:
    print("ДА")