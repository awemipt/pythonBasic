import math

n = int(input())

for num in range(2, n):
    for divisor in range(2, num):
        # print(j)
        if num % divisor == 0:
            break
    else:
        print(num)
    # print()
