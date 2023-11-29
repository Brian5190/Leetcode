nums = [3,2,2,3]
val = 3
k = 0
for i in range(0,len(nums)):
    print(i)
    if nums[i] != val:
        nums[k] = nums[i]
        k = k + 1
                
print(k,nums)