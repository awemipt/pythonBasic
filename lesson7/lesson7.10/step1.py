def counter_add():
    def add(num):
        return num + 5

    return add


k = int(input())
cnt = counter_add()
print(cnt(k))
