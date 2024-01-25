class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            d[i] = 1 + d.get(i, 0)
        value_list = list(d.values())
        return len(value_list) == len(set(value_list))