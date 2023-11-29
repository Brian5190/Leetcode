
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for i in ransomNote:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in magazine:
                if i in dic:
                    dic[i] = dic[i]-1
        for i in ransomNote:
            if dic[i] > 0:
                return False
        return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if ransomNote.count(i)-magazine.count(i) > 0:
                return False
        return True