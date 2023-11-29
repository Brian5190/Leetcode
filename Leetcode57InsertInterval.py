class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #merge
        intervals.append(newInterval)
        intervals = sorted(intervals)
        left = intervals[0][0]
        right = intervals[0][1]
        l = []
        for i in range(len(intervals)):
            if intervals[i][0] <= right:
                right = max(right,intervals[i][1])
            elif intervals[i][0] > right:
                l.append([left,right])
                left = intervals[i][0]
                right = intervals[i][1]
        l.append([left,right])
        return(l)
