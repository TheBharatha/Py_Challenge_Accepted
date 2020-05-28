class Solution:
    def __init__(self):
        self.sumArray = list()
        
    def countBits(self, num):
        while num >= 0:
            binary = int(bin(num)[2:])
            self.sumArray.insert(0,sum(list(map(int,str(binary)))))
            num -= 1
        
        return self.sumArray

if __name__ == "__main__":
    num = 5
    obj = Solution()
    print(obj.countBits(num))