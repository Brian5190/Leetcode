class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        temp = []
        res = []
        for i in range(row * col):
            x = i // col
            y = i % col
            a_0, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8 = 0, 0, 0, 0, 0, 0, 0, 0, 0
            val = 0
            num = 0
            if x - 1 in range(0, row) and y - 1 in range(0, col):
                a_0 = img[x - 1][y - 1]
                val += a_0
                num += 1
            if y - 1 in range(0, col):
                a_1 = img[x][y - 1]
                val += a_1
                num += 1
            if x + 1 in range(0, row) and y - 1 in range(0, col):
                a_2 = img[x + 1][y - 1]
                val += a_2
                num += 1
            if x - 1 in range(0, row):
                a_3 = img[x - 1][y]
                val += a_3
                num += 1
            a_4 = img[x][y]
            val += a_4
            num += 1
            if x + 1 in range(0,row):
                a_5 = img[x + 1][y]
                val += a_5
                num += 1
            if x - 1 in range(0, row) and y + 1 in range(0, col):
                a_6 = img[x - 1][y + 1]
                val += a_6
                num += 1
            if y + 1 in range(0, col):
                a_7 = img[x][y + 1]
                val += a_7
                num += 1
            if x + 1 in range(0, row) and y + 1 in range(0, col):
                a_8 = img[x + 1][y + 1]
                val += a_8
                num += 1
            temp.append(val // num)
            if i % col == col - 1:
                res.append(temp)
                temp = []
            
        return res