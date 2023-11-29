nums = [2,3,1,1,1]
k = 0
l = r =0

while r < len(nums) - 1:
    b = 0
    for j in  range(l,r+1):
        b = max(b, nums[j]+j)
    l = r + 1
    r = b
    k += 1
print(k)