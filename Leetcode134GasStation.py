class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        station = 0
        sub = []
        for i in range(len(gas)):
            sub.append(gas[i]-cost[i])
        result = 0
        if sum(sub) < 0:
            return -1
        for i in range(len(gas)):
            result += sub[i]
            if result < 0:
                station = i + 1
                result = 0
        return station