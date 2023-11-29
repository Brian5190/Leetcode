class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9:
            return False
        for i in board:
            if len(i) != 9:
                return False
        reboard = [''] * 9
        reboard2 = [''] * 9
        s1, s2, s3, s4, s5, s6, s7, s8, s9 = '', '', '', '', '', '', '', '', ''
        for i in range(9):
            for j in range(9):
                if i // 3 == 0:
                    if j // 3 == 0:
                        s1 += board[i][j]
                if i // 3 == 1:
                    if j // 3 == 0:
                        s2 += board[i][j]
                if i // 3 == 2:
                    if j // 3 == 0:
                        s3 += board[i][j]

                if i // 3 == 0:
                    if j // 3 == 1:
                        s4 += board[i][j]
                if i // 3 == 1:
                    if j // 3 == 1:
                        s5 += board[i][j]
                if i // 3 == 2:
                    if j // 3 == 1:
                        s6 += board[i][j]

                if i // 3 == 0:
                    if j // 3 == 2:
                        s7 += board[i][j]
                if i // 3 == 1:
                    if j // 3 == 2:
                        s8 += board[i][j]
                if i // 3 == 2:
                    if j // 3 == 2:
                        s9 += board[i][j]         
        reboard2[0] = list(s1)
        reboard2[1] = list(s2)
        reboard2[2] = list(s3)
        reboard2[3] = list(s4)
        reboard2[4] = list(s5)
        reboard2[5] = list(s6)
        reboard2[6] = list(s7)
        reboard2[7] = list(s8)
        reboard2[8] = list(s9)
        for i in range(9):
            l = []
            for j in range(9):
                l.append(board[j][i])
            reboard[i] = l
        for i in range(9):
            l1 = reboard[i]
            l2 = board[i]
            l3 = reboard2[i]
            for j in range(8):
                if l1[j] != '.':
                    if l1[j] in l1[j+1:]:
                        return False
                if l2[j] != '.':
                    if l2[j] in l2[j+1:]:
                        return False
                if l3[j] != '.':
                    if l3[j] in l3[j+1:]:
                        return False
        return True