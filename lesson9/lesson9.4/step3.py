nums = map(int, input().split())
nums = filter(lambda x: 9 < abs(x) < 100, nums)
print(*nums)