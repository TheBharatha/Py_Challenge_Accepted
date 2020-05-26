class Solution:
    def findMaxLength(self, nums):
        if nums is None or len(nums) < 2: 
            return 0
        arrayLen = len(nums)
        subArray = 0
        arrayIndex = {0:-1}
        stepBack = 0
        for i in range(arrayLen):
            if nums[i] == 1:
                stepBack += 1
            else:
                stepBack -= 1
            if stepBack not in arrayIndex:
                arrayIndex[stepBack] = i
            else:
                subArray = max(subArray, i-arrayIndex[stepBack])
        return subArray