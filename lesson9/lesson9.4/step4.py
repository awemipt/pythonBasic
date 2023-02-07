coins1 = set(map(int, input().split()))
coins2 = set(map(int, input().split()))
res = filter(lambda x: x % 2 ==0, coins2 & coins1)
print(*res)