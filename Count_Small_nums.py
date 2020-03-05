#Method 1 using len fumction
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smalls = list()
        for num in nums:
            smalls.append(len([nums[i] for i in range(len(nums)) if nums[i] < num]))
        return(smalls)

#Method 2 using map function
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smalls = list()
        for num in nums:
            smalls.append(sum(map(lambda i: i < num, nums)))
        return(smalls)
        
#Test case
#nums = [8,2,3,1,0,5,8,1,4,0,3,5,6,7,3,8,0,1,2,4,6,5,7,8,0,7,1,2,6]
#nums = [8,1,2,2,3]
#nums = [6,5,4,8]
#nums = [7,7,7,7]
