class Solution:
    def shuffle(self, nums, n):
        a = nums[:n]
        b = nums[n:]
        aAndB = list()
        stop = True
        index = 0
        while stop:
            aAndB.insert(len(aAndB), a[index])
            aAndB.insert(len(aAndB), b[index])
            index+=1
            if index == n:
                stop = False
        return(aAndB)