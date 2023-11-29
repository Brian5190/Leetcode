class Solution:
    def reverseWords(self, s: str) -> str:
        string_List = s.split()
        l = len(string_List)
        reverse_List = []
        for i in range(l):
            reverse_List.append(string_List[l-1-i])
        
        return ' '.join(reverse_List)