class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        self.given = nums
        self.nums = sorted(set(nums))
        result = list(filter( lambda x: self.given.count(x) == 1, self.nums))
        return(result[0])
