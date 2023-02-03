nums = list(map(float, input().split()))
nums = [x for i,x in enumerate(nums)  if i %2 ==0]
print(*nums)