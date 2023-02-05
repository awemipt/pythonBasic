nums = list(map(int, input().split()))
d = {}
for num in nums:
    d.setdefault(num, 1)
print(*d)