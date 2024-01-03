class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        l = [[] for i in range(len(board))]
        col = len(board[0])
        row = len(board)
        #copy matrix

        for i in range(row):
            for j in range(col):
                temp_0 = 0
                temp_1 = 0
                if 0 <= i - 1 <= row - 1:
                    if board[i - 1][j] == 0:
                        temp_0 += 1
                    else:
                        temp_1 += 1
                if 0 <= i + 1 <= row - 1:
                    if board[i + 1][j] == 0:
                        temp_0 += 1
                    else:
                        temp_1 += 1
                if 0 <= j - 1 <= col - 1:
                    if board[i][j - 1] == 0:
                        temp_0 += 1
                    else:
                        temp_1 += 1
                if 0 <= j + 1 <= col - 1:
                    if board[i][j + 1] == 0:
                        temp_0 += 1
                    else:
                        temp_1 += 1
                if 0 <= i - 1 <= row - 1 and 0 <= j - 1 <= col - 1:
                    if board[i - 1][j - 1] == 0:
                        temp_0 += 1
                    else:
                        temp_1 += 1
                if 0 <= i + 1 <= row - 1 and 0 <= j - 1 <= col - 1:
                    if board[i + 1][j - 1] == 0:
                        temp_0 += 1
                    else:
                        temp_1 += 1
                if 0 <= i - 1 <= row - 1 and 0 <= j + 1 <= col - 1:
                    if board[i - 1][j + 1] == 0:
                        temp_0 += 1
                    else:
                        temp_1 += 1
                if 0 <= i + 1 <= row - 1 and 0 <= j + 1 <= col - 1:
                    if board[i + 1][j + 1] == 0:
                        temp_0 += 1
                    else:
                        temp_1 += 1                    
                if temp_1 == 3 and board[i][j] == 0:
                    l[i].append(1)
                elif (temp_1 < 2 or temp_1 > 3) and board[i][j] == 1:
                    l[i].append(0)
                else:
                    l[i].append(board[i][j])
        #copy result
        for i in range(row):
            board[i] = l[i]
        
                    
