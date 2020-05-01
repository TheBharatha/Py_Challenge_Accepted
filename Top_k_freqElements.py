class Solution:
    def topKFrequent(self, nums, k):
        uniqueNums = sorted(set(nums))
        freqElements = dict(map(lambda x: (x, nums.count(x)), uniqueNums))
        freqElements = sorted(freqElements.items(), key = lambda y:y[1], reverse = True)
        freqElements = list(map(lambda x: x[0], freqElements[:k]))
        return(freqElements)


if __name__ == '__main__':
    solObject = Solution()
    nums = [1,1,1,2,2,2,2,2,3,4,4,4,4,4,4]
    k = 2
    result = solObject.topKFrequent(nums,k)
    print(result)