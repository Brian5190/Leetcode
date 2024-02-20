class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for i in arr:
            d[i] = 1 + d.get(i, 0)
        #sort by value
        d = sorted(d.items(), key = lambda x:x[1])
        #conver tuple to dict
        d = dict((x,y) for x, y in d)
        for i in d:
            temp = min(d[i], k)
            d[i] -= temp
            k -= temp
            if k == 0:
                break
        #find key which value > 0
        return len([key for key, i in d.items() if i > 0])
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for i in arr:
            d[i] = 1 + d.get(i, 0)
        #just consider values of dict
        val = sorted(d.values())
        for i in range(len(val)):
           temp = min(val[i], k)
           val[i] -= temp
           k -= temp
           if k == 0:
               break
        return len([i for i in val if i > 0])
