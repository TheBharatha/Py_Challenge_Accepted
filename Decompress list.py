#LeetCode, Decompress Run-Length Encoded List
nums = [42,39,12,1,2,3,4,5,6,0,2]
rep = list()
i = 0
if 2 <= len(nums) <= 100:
    while i != len(nums)-1:
        if i%2 == 0 and 1 <= nums[i] <= 100:
            for j in range(nums[i]):
                rep.append(nums[i+1])
        i += 1
        j = 0
print(rep)
