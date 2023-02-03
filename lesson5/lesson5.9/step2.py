nums = list(map(int, input().split()))
n = int(len(nums)**.5)
print([[nums[n*j+ i] for i in range(n)] for j in range(n)])