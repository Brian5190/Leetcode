class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        l = access_times
        for i in l:
            k = int(i[1])/100
            i[1] = int(k)*60 + int(i[1])%100
        l2 = []
        l = sorted(l)
        for i in range(len(l)):
            k = 0
            t = l[i][1]
            tt=0
            for j in range(i,len(l)): 
                if l[i][0] == l[j][0] and (l[j][1] - t)<= 59 - tt:
                    k += 1
                    tt = (l[j][1]-t)
                    t = l[j][1]
            if k >= 3:
                l2.append(l[i][0])
        return list(set(l2))
