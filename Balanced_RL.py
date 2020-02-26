class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 1
        for i in range(1,len(s)):
            rl = s[:i]
            if rl.count('R') == rl.count('L'):
                count += 1
        return(count)
