class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        d = {}
    
        for i in range(len(word) // k):
            d[word[i * k: (i + 1) * k ]] = 1 + d.get(word[i * k: (i + 1) * k ], 0)
        
        l = list(d.values())
        return sum(l) - max(l)