hours = int(input())
n = 1
i = 1
while i < hours:
    if i%3==0:
        n*=2
    i += 1
print(n)