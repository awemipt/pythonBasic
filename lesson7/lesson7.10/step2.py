def counter_add(n):
    def add(num):
        return num + n

    return add


k = int(input())
cnt = counter_add(2)
print(cnt(k))
