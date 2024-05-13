class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            if grid[i][0] != 1:
                for j in range(col):
                    grid[i][j] = (grid[i][j] + 1) % 2
        for i in range(col):
            cout = 0
            for j in range(row):
                if grid[j][i] == 1:
                    cout += 1
            if cout <= (row / 2):
                for j in range(row):
                    grid[j][i] = (grid[j][i] + 1) % 2
        
        res = 0
        for i in range(row):
            num = 0
            for j in range(col):
                num = 2 * num + grid[i][j]
            res += num
        return res