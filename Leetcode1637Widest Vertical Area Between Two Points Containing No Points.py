class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        def first(x):
            return x[0]
        points.sort(key = first)
        temp = 0
        for i in range(len(points) - 1):
            if points[i + 1][0] - points[i][0] > temp:
                temp = points[i + 1][0] - points[i][0]
        return temp