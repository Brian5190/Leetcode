class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        transport_grid = [[0] * len(grid) for i in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                transport_grid[j][i] = grid[i][j]
        num_List1 = []
        num_List2 = []
        for i in grid:
            num_List1.append(sum(i) - (len(i) - sum(i)))
        for i in transport_grid:
            num_List2.append(sum(i) - (len(i) - sum(i)))
        temp_List = []
        i = 0
        while i < len(grid) * len(grid[0]):
            row = i // len(grid[0])
            col = i % len(grid[0])
            temp_List.append(num_List1[row] + num_List2[col])
            if col == len(grid[0]) - 1:
                res.append(temp_List)
                temp_List = []
            i += 1
        return res