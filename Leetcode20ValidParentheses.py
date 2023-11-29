class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        slist = list(s)
        k = 1
        while(k == 1):
            if len(slist) == 0 :
                break
            for i in range(len(slist)-1):
                if slist[i] == '[' and slist[i + 1] == ']':
                    del slist[i:i+2]
                    break
                if slist[i] == '(' and slist[i + 1] == ')':
                    del slist[i:i+2]
                    break
                if slist[i] == '{' and slist[i + 1] == '}':
                    del slist[i:i+2]
                    break
                if i == len(slist) - 2:
                    k = 0
                    break
        if len(slist) == 0:
            return True
        return False
class Solution:
    def isValid(self, s: str) -> bool:
        stackList = []
        pairsDict = {'(':')', '[':']', '{':'}'}

        for bracket in s:
            if bracket in pairsDict:
                stackList.append(bracket)
            elif len(stackList) == 0 or bracket != pairsDict[stackList.pop()]:
                return False
        return len(stackList) == 0
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowD = {}
        colD = {}
        sqD = {}
        for i in range(9):
            rowD[i] = []
            colD[i] = []
        for i in range(3):
            for j in range(3):
                sqD[(i % 3, j % 3)] = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in rowD[i] or board[i][j] in colD[j] or board[i][j] in sqD[(i // 3, j // 3)]:
                        return False
                    else:
                        rowD[i].append(board[i][j])
                        colD[j].append(board[i][j])
                        sqD[(i // 3, j // 3)].append(board[i][j])
        return True