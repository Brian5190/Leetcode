class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
            
        nums[:] = nums[n-k:]+nums[:n-k]  
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums1 = []
        k = k % len(nums)
        if len(nums) != 1:
            
            for i in range(len(nums)-k):
                nums1.append(nums[i])
            for j in range(k):
                nums[j] = nums[j+len(nums)-k]
            for a in range(len(nums)-k):
                nums[a+k] = nums1[a]
