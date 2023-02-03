numbers = list(map(int, input().split()))

jMin = 0
for i in range(len(numbers)):
    m = numbers[i]
    jMin = i
    for j in range(i+1, len(numbers)):
        if numbers[j] < m:
            m = numbers[j]
            jMin = j

    numbers[i],numbers[jMin] = numbers[jMin], numbers[i]

print(*numbers)