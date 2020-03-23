class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = list()
        for ind in range(len(nums)):
            result.insert(index[ind], nums[ind])
        return(result)
