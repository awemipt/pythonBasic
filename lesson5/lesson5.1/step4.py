n = int(input())
i = 1
sum = 0
while i < n + 1:
    sum += 1/i
    i += 1
print(round(sum,3))