class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        eCount = 0
        for value in nums:
            if len(str(value))%2 == 0:
                eCount += 1
        return eCount
