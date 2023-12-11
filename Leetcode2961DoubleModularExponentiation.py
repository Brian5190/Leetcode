class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i in range(len(variables)):
            var_0, var_1, var_2, var_3 = variables[i]
            if (((var_0 ** var_1) % 10) ** var_2) % var_3 == target:
                res.append(i)
        return res