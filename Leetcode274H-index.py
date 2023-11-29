citations = [1,2,3,4,5]
k = 0
for i in range(1,len(citations)+1):
    temp = 0
    for j in citations:
        print(i,j)
        
        if j >= i:
            temp += 1
        if temp >= i:
            k = i
print(k)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        l = len(citations)
        for i in range(l):
            if citations[i] >= l - i:
                return l - i
        return 0