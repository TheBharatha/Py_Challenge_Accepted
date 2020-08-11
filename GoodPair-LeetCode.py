class Solution:
    def numIdenticalPairs(self, nums):
        goodPair = 0
        for position in range(len(nums)):
            if nums[position] in nums[position+1:]:
                goodPair += nums[position+1:].count(nums[position])
        return(goodPair)