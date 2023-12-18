class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_num = len(words)
        word_Len = len(words[0])
        res = []
        count = 0
        word_dic = {}

        for i in words:
            word_dic[i] = 1 + word_dic.get(i, 0)

        for j in range(word_Len):
            i = j

            while i <= len(s) - word_Len:
                if s[i - word_num * word_Len: i - word_num * word_Len + word_Len] in word_dic and i >= word_num * word_Len:
                    word_dic[s[i - word_num * word_Len: i - word_num * word_Len + word_Len]] += 1
                    if word_dic[s[i - word_num * word_Len: i - word_num * word_Len + word_Len]] == 1:
                        count -= 1

                if s[i: i + word_Len] in word_dic:
                    word_dic[s[i: i + word_Len]] -= 1
                    if word_dic[s[i: i + word_Len]] == 0:
                        count += 1
                    if count == len(word_dic):
                        res.append(i - (word_num - 1) * word_Len)
                i += word_Len
            count = 0
            for m in word_dic:
                word_dic[m] = 0
            for m in words:
                word_dic[m] = 1 + word_dic.get(m, 0)
        return res