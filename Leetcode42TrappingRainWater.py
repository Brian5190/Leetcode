class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        left = 0
        right = 0
        temp = []
        result = 0
        for i in range(len(height)):
            right = i
            temp.append(height[i])
            
            if height[right] >= height[left]:

                if height[left] > min(temp) and height[right] > min(temp):
                    result += min(height[right], height[left]) * len(temp) - sum(temp) + abs(height[right] - height[left])

                temp = []
                left = right
                temp.append(height[i])

        right = len(temp) - 1
        left = len(temp) - 1

        if len(temp) > 2:
            temp2 = []

            for i in range(len(temp) - 1, -1, -1):
                left = i
                temp2.append(temp[i])

                if temp[right] <= temp[left]:

                    if temp[right] > min(temp2) and temp[left] > min(temp2):
                        result += min(temp[right], temp[left]) * len(temp2) - sum(temp2) + abs(temp[right] - temp[left])
                        
                    right = left
                    temp2 = []
                    temp2.append(temp[i])
        return result
                    