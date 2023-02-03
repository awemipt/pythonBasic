n = int(input())
i = 1
if n > 100:
    print('слишком большое значение n')
else:
    while i < n:
        if i % 15 == 0:
            print(i, end=' ')
        i+=1
