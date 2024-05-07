class Solution:
    def isValid(self, word: str) -> bool:
        
        if len(word) < 3:
            return False
        
        vowel = ['a', 'e', 'i', 'o', 'u']
        word = word.lower()
        count = [0] * 3
        for i in word:
            #print(i, ord(i))
            if ord(i) in range(48, 58):
                count[0] = 1
            elif i in vowel:
                count[1] = 1
            else:
                if ord(i) in range(97, 123):
                    count[2] = 1
            if 48 > ord(i) or 57 < ord(i) < 97 or ord(i) > 122:
                return False
        #print(count)
        return count == [1, 1, 1] or count == [0, 1, 1]
