nums = tuple(map(int, input().split()))
uniqe = []
for num in nums:
    if nums.count(num) > 1:
        i =0
        while(num not in uniqe and num in nums[i:] and nums.index(num,i)!=-1):
            print(nums.index(num, i), end= ' ')
            i = nums.index(num,i)+1
        uniqe.append(num)