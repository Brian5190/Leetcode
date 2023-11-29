class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i ,j in enumerate(numbers):
            if j not in dic:
                dic[target - j] = i + 1
            else: return dic[j], i+1 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i ,j in enumerate(numbers):
            if j not in dic:
                dic[target - j] = i + 1
            else: return dic[j], i+1 