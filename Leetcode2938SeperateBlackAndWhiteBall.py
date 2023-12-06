class Solution:
    def minimumSteps(self, s: str) -> int:
        left = 0
        right = 0
        dis = 0
        
        while(right < len(s)):
            
            if s[right] == '0':
                dis += right - left
                left += 1
                
            right += 1
        
        return dis