nums1 = map(int, input().split())
nums2 = map(int, input().split())
nums = zip(nums1, nums2)
for i in range(3):
    a, b = next(nums)
    print(a * b, end=' ')