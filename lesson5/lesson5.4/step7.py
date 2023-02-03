nums = list(map(float, input().split()))
for i, num in enumerate(nums):
    if num < 0:
        nums[i] = -1.0
print(*nums)