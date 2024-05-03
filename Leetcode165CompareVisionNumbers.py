class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lv1 = version1.split('.')
        lv2 = version2.split('.')

        #make both length the same.     
        if (len(lv1) > len(lv2)):
            for i in range(len(lv1) - len(lv2)):
                lv2.append(0)
        else:
            for i in range(len(lv2) - len(lv1)):
                lv1.append(0)
        #compare. 
        for i in range(len(lv1)):
            if int(lv1[i]) > int(lv2[i]):
                return 1
            elif int(lv1[i]) < int(lv2[i]):
                return -1
        return 0
