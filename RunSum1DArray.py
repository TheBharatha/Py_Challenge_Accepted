class Solution:
    def runningSum(self, nums):
        sumNow = 0
        for position in range(len(nums)):
            sumNow += nums[position]
            nums[position] = sumNow
        return nums