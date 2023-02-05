nums = tuple(map(int, input().split()))
unique_nums = ()
for num in nums:
    if num not in unique_nums:
        unique_nums += num,
print(*unique_nums)