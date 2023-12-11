class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        result = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0:
                result += 1
                for j in range(i, len(batteryPercentages)):
                    batteryPercentages[j] -= 1
        return result