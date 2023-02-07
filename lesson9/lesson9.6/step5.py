nums1 = [int(x) for x in input().split()]
nums2 = [int(x) for x in input().split()]
nums1.sort()
nums2.sort(reverse=True)
for x, y in zip(nums1, nums2):
    print(x+y, end=' ')