class Solution:
    def reverse(self, x):
        if not x < 0:
            y = int(str(x)[::-1])
        else:
            x = x * -1
            y = int(str(x)[::-1]) * -1
        
        if y <= -2**31 or y >= 2**31 - 1:
            y = 0
        
        return(y)

if __name__ == '__main__':
    get = Solution()
    around = get.reverse(-2147483648)
    print(around)
