class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        delta = [] 
        for i in range(1, len(heights)):
            if heights[i] > heights[i - 1]:
                heapq.heappush(delta, heights[i] - heights[i - 1])
                if len(delta) > ladders:
                    bricks -= heapq.heappop(delta)
                if bricks < 0:
                    return i - 1
        return len(heights) - 1