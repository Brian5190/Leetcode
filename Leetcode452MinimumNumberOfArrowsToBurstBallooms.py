class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
            points = sorted(points)
            k = 0
            shoot = 0
            left = points[0][0]
            right = points[0][1]

            while(k < len(points)):
                if right >= points[k][0]:
                    if right >= points[k][1]:
                        right = points[k][1]
                    k += 1
                elif right < points[k][0]:
                    shoot += 1
                    left = points[k][0]
                    right = points[k][1]
                    k += 1
            
            return shoot + 1