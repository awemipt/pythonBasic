nums = map(float, input().split())
m = next(nums)
for i in nums:
    if i < m:
        m = i

print(m)