class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for string in strs:
            temp_sorted = ''.join(sorted(string))
            if temp_sorted not in dic:
                dic[temp_sorted] = []
            dic[temp_sorted].append(string)
        return list(dic.values())