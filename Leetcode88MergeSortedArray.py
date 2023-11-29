nums1 = [1,2,3,0,0,0]
nums2 = [3,2,1]
m = 3
n = 3
j  = 0
while m < len(nums1):
    nums1[m] = nums2[j]
    m += 1
    j += 1
nums1.sort()
print(nums1)